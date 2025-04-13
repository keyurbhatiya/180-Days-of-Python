# 63 : Pomodoro Timer App

import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg="green")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg="red")
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg="pink")
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work", fg="green")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    mins = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="black")

title_label = tk.Label(text="Timer", fg="green", bg="black", font=("Courier", 35, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg="black", highlightthickness=0)
# tomato_img = tk.PhotoImage(file="tomato.png")  # Optional: add tomato.png in the same directory
canvas.create_image(100, 112,)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 30, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightbackground="black", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightbackground="black", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg="white", bg="black", font=("Courier", 20, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()


