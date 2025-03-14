import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import SneakySnapBackend as backend

class SneakySnapGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SneakySnap Application")

        # Webhook Input
        self.webhook_label = tk.Label(root, text="Discord Webhook URL:")
        self.webhook_label.pack(pady=5)
        self.webhook_entry = tk.Entry(root, width=50)
        self.webhook_entry.pack(pady=5)
        self.test_webhook_button = tk.Button(root, text="Test Webhook", command=self.test_webhook)
        self.test_webhook_button.pack(pady=5)

        # Delay Input
        self.delay_label = tk.Label(root, text="Delay Between Photos (seconds):")
        self.delay_label.pack(pady=5)
        self.delay_entry = tk.Entry(root, width=10)
        self.delay_entry.insert(0, "5")  # Default 5 seconds
        self.delay_entry.pack(pady=5)
        self.set_delay_button = tk.Button(root, text="Set Delay", command=self.set_delay)
        self.set_delay_button.pack(pady=5)
        self.delay_value = tk.Label(root, text="Current Delay: 5 seconds")
        self.delay_value.pack(pady=5)

        # Control Buttons
        self.start_button = tk.Button(root, text="Start Capture", command=self.start_capture, state=tk.DISABLED)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(root, text="Stop Capture", command=self.stop_capture, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        # Log Display
        self.log_text = tk.Text(root, height=10, width=60, state=tk.DISABLED)
        self.log_text.pack(pady=10)

        # Backend Initialization
        self.backend = backend.SneakySnapBackend(self.log_callback)
        self.log_callback("Application initialized and ready.")

    def log_callback(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def test_webhook(self):
        webhook_url = self.webhook_entry.get().strip()
        if not webhook_url:
            messagebox.showerror("Error", "Please enter a webhook URL.")
            return
        result = self.backend.test_webhook(webhook_url)
        if result:
            messagebox.showinfo("Success", "Webhook test successful!")
            self.start_button.config(state=tk.NORMAL)  # Enable Start only if webhook works
        else:
            messagebox.showerror("Error", "Webhook test failed. Check URL and try again.")

    def set_delay(self):
        try:
            delay = int(self.delay_entry.get().strip())
            if delay <= 0:
                raise ValueError("Delay must be positive.")
            self.delay_value.config(text=f"Current Delay: {delay} seconds")
            self.backend.set_delay(delay)
            self.log_callback(f"Delay set to {delay} seconds.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for delay.")
            self.delay_entry.delete(0, tk.END)
            self.delay_entry.insert(0, "5")

    def start_capture(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.backend.start_capture(self.webhook_entry.get().strip())

    def stop_capture(self):
        self.backend.stop_capture()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SneakySnapGUI(root)
    root.mainloop()