# SneakySnap

SneakySnap is a Python-based application designed to capture webcam photos at user-defined intervals and send them to a Discord webhook. It features a clean GUI for configuration and a robust backend for processing, with detailed logging for transparency and debugging.

## Features
- **Customizable Delay**: Set the interval (in seconds) between photo captures.
- **Dynamic Webhook**: Input and test your Discord webhook URL within the app.
- **Continuous Capture**: Loop photo capture until manually stopped.
- **Professional Logging**: Detailed logs saved to `SneakySnap.log` and displayed in the GUI.
- **Modular Design**: Separates frontend (`SneakySnapGUI.py`) and backend (`SneakySnapBackend.py`) for maintainability.

## Installation

### Prerequisites
- **Python 3.x**: Ensure Python 3.6 or higher is installed. Download from [python.org](https://www.python.org/downloads/).
- **pip**: Python package manager (usually included with Python).

### Required Libraries
Install the necessary dependencies via pip:
```bash
pip install opencv-python requests tkinter pyinstaller

opencv-python: For webcam access and image capture.

requests: For sending photos to the Discord webhook.

tkinter: Built-in Python library for the GUI (no separate install needed).

pyinstaller: For building the application into a standalone executable.

Setup
Clone the Repository:
bash

git clone https://github.com/yourusername/SneakySnap.git
cd SneakySnap

(Replace yourusername with your GitHub username once you push this.)

Install Dependencies:
Run the pip command above to install all required libraries.

Verify Installation:
Ensure Python and libraries are installed:
bash

python --version
pip list

Usage
Running the Application
Launch the GUI:
bash

python SneakySnapGUI.py

The application window will open with fields for webhook URL and delay settings.

Configure the Webhook:
Enter your Discord webhook URL (e.g., https://discord.com/api/webhooks/...).

Click Test Webhook to verify it works. A successful test enables the "Start Capture" button.

Set Delay:
Enter a number (in seconds) in the delay field (e.g., 10).

Click Set Delay to apply it. The current delay will update in the GUI.

Start Capture:
Click Start Capture to begin taking photos at the set interval. Photos are sent to the webhook.

Logs will appear in the GUI and SneakySnap.log.

Stop Capture:
Click Stop Capture to halt the process.

Building an Executable
To create a standalone .exe for distribution:
Build Backend:
bash

pyinstaller --onefile SneakySnapBackend.py

Build GUI with Backend:
bash

pyinstaller --onefile --add-data "SneakySnapBackend.py;." SneakySnapGUI.py

Run:
Find SneakySnapGUI.exe in the dist folder and execute it.

Project Structure
SneakySnapGUI.py: Frontend GUI for user interaction.

SneakySnapBackend.py: Backend logic for webcam capture and webhook communication.

SneakySnap.log: Log file generated during runtime with detailed process information.

Log File
The SneakySnap.log file records all actions with timestamps and log levels:
Format: YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE

Example:

2025-03-14 12:34:56 - INFO - Backend initialized.
2025-03-14 12:35:00 - INFO - Webhook test passed successfully.
2025-03-14 12:35:05 - INFO - Image captured successfully at 12:35:05.
2025-03-14 12:35:06 - ERROR - Webhook request failed: 429 - Too Many Requests

Purpose: Provides a detailed audit trail for debugging and monitoring.

Troubleshooting
Webcam Not Detected: Ensure your webcam is connected and accessible. Check logs for "Webcam not detected" errors.

Webhook Fails: Verify the URL is correct and test it manually with curl:
bash

curl -X POST -F "content=test" YOUR_WEBHOOK_URL

GUI Errors: Run with Python directly (python SneakySnapGUI.py) to see detailed error messages.

TODO
Future enhancements to expand functionality:
Stealth Mode:
Minimize to system tray or run silently without a visible window.

Hide process from task manager (if possible).

Persistence Mechanism:
Add startup registry entry or scheduled task for automatic execution on system boot.

Ensure the app restarts after closure or system reboot.

Encryption:
Encrypt captured images before sending to the webhook.

Secure log file contents with basic encryption.

Remote Control:
Implement a command system via Discord (e.g., start/stop capture remotely).

Allow configuration updates through a remote interface.

Keylogging or Screen Capture:
Add keylogging to capture user input alongside photos.

Include periodic screen captures as an alternative to webcam photos.

Anti-Detection Measures:
Obfuscate the executable to evade basic antivirus scans.

Randomize file names and signatures for each build.

Contributing
Feel free to fork this repository, submit pull requests, or open issues for bugs and feature requests.
License
This project is unlicensed—use at your own risk. Intended for educational purposes only.

