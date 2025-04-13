# **64.** Flashcard App (quiz mode)

import tkinter as tk
from tkinter import messagebox

# Flashcard data (You can load from a JSON or CSV too)
flashcards = {
    "Python keyword for function": "def",
    "Color of the sky": "Blue",
    "PIP package manager for Python": "Pip",
    "Keyword to define a class in Python": "class",
    "Data type for True or False values": "bool",
    "Function used to output text in Python": "print",
    "Keyword to import a module": "import",
    "Method to add an item to a list": "append",
    "Loop that runs while a condition is True": "while",
    "Loop that iterates over a sequence": "for",
    "Function to get the length of a list": "len",
    "Special method to initialize objects": "__init__",
    "Keyword to handle exceptions": "try",
    "Keyword used with try to catch exceptions": "except",
    "Python file extension": ".py",
    "Built-in type for a dictionary": "dict",
    "Used to define an anonymous function": "lambda",
    "Convert string to integer": "int()",
    "API Full Name": "Application Programming Interface",
}


class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcard Quiz App")

        self.questions = list(flashcards.keys())
        self.index = 0
        self.score = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.submit_btn = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=10)

        self.feedback_label = tk.Label(master, text="", font=("Arial", 12))
        self.feedback_label.pack()

        self.next_question()

    def next_question(self):
        if self.index < len(self.questions):
            self.question_label.config(text=f"Q{self.index+1}: {self.questions[self.index]}")
            self.entry.delete(0, tk.END)
            self.feedback_label.config(text="")
        else:
            messagebox.showinfo("Quiz Finished", f"Your Score: {self.score}/{len(self.questions)}")
            self.master.quit()

    def check_answer(self):
        user_answer = self.entry.get().strip()
        correct_answer = flashcards[self.questions[self.index]]

        if user_answer.lower() == correct_answer.lower():
            self.feedback_label.config(text="✅ Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"❌ Wrong! Correct: {correct_answer}", fg="red")

        self.index += 1
        self.master.after(1000, self.next_question)

# Run the app
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
