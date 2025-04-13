import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample text pool
sentences = [
    "Python is a powerful programming language.",
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed is measured in words per minute.",
    "Practice daily to improve your typing accuracy.",
    "Debugging code can be challenging but rewarding."
]

class TypingTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.text_to_type = random.choice(sentences)

        self.start_time = None

        self.label = tk.Label(master, text="Type the following:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.text_display = tk.Label(master, text=self.text_to_type, wraplength=500, font=("Arial", 12))
        self.text_display.pack(pady=10)

        self.entry = tk.Text(master, height=4, font=("Arial", 12), wrap="word")
        self.entry.pack(pady=10)

        self.entry.bind("<FocusIn>", self.start_timer)

        self.button = tk.Button(master, text="Submit", command=self.calculate_speed)
        self.button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        if self.start_time is None:
            messagebox.showwarning("Warning", "Click inside the text box to start typing first!")
            return

        end_time = time.time()
        time_taken = end_time - self.start_time

        typed_text = self.entry.get("1.0", tk.END).strip()

        words_typed = len(typed_text.split())
        original_words = self.text_to_type.split()

        # Calculate accuracy
        correct_words = 0
        for i in range(min(len(typed_text.split()), len(original_words))):
            if typed_text.split()[i] == original_words[i]:
                correct_words += 1
        accuracy = (correct_words / len(original_words)) * 100

        # WPM calculation
        wpm = (words_typed / time_taken) * 60

        messagebox.showinfo("Results", f"Time Taken: {round(time_taken, 2)} seconds\nWPM: {int(wpm)}\nAccuracy: {int(accuracy)}%")

        self.reset_test()


    def reset_test(self):
        self.text_to_type = random.choice(sentences)
        self.text_display.config(text=self.text_to_type)
        self.entry.delete("1.0", tk.END)
        self.start_time = None

# Run the app
root = tk.Tk()
app = TypingTestApp(root)
root.mainloop()
