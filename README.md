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
```
Setup
Clone the Repository
```bash
git clone https://github.com/jeffrey-steve/SneakySnap.git
cd SneakySnap``



