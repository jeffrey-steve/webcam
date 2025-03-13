import tkinter as tk
from tkinter import ttk
import SneakySnapBackend as backend

class SneakySnapGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SneakySnap Application")

        # Initialize UI elements first
        self.delay_label = tk.Label(root, text="Delay Between Photos (seconds):")
        self.delay_label.pack(pady=5)

        self.delay_slider = ttk.Scale(root, from_=1, to=60, orient=tk.HORIZONTAL, length=300)
        self.delay_slider.set(5)  # Default 5 seconds
        self.delay_slider.pack(pady=5)

        self.delay_value = tk.Label(root, text=f"Current Delay: {int(self.delay_slider.get())} seconds")
        self.delay_slider.bind("<Motion>", lambda e: self.update_delay_label())
        self.delay_value.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Capture", command=self.start_capture)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Capture", command=self.stop_capture, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.log_text = tk.Text(root, height=10, width=60, state=tk.DISABLED)
        self.log_text.pack(pady=10)

        # Now initialize backend with log callback
        self.backend = backend.SneakySnapBackend(self.log_callback)
        self.log_callback("Application initialized and ready.")

    def update_delay_label(self):
        self.delay_value.config(text=f"Current Delay: {int(self.delay_slider.get())} seconds")

    def log_callback(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def start_capture(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        delay = int(self.delay_slider.get())
        self.backend.start_capture(delay)

    def stop_capture(self):
        self.backend.stop_capture()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SneakySnapGUI(root)
    root.mainloop()