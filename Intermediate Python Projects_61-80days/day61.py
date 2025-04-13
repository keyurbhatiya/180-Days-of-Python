# **61.** Digital Clock GUI using `tkinter`

import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S %p')  # 24-hour format with AM/PM
    label.config(text=current_time)
    label.after(1000, time)  # update every 1000 ms (1 second)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')

# Configure window size and background
root.geometry('400x200')
root.configure(bg='black')

# Create a label for time display
label = tk.Label(root, font=('Arial', 50, 'bold'), bg='black', fg='cyan')
label.pack(anchor='center', expand=True)

# Call the time function
time()

# Run the app
root.mainloop()

