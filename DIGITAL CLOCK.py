import tkinter as tk
import time
import random

def update_time():
    current_time = time.strftime('%I:%M:%S %p')  # Use %I for 12-hour format, %p for AM/PM
    label.config(text=current_time, fg=get_random_color())
    label.after(1000, update_time)

def get_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

root = tk.Tk()
root.title("Digital Clock")

# Set the desired font and size
font_style = ('Comic Sans MS', 80)

label = tk.Label(root, font=font_style, bg='black')
label.pack(padx=50, pady=50)

update_time()

root.mainloop()
