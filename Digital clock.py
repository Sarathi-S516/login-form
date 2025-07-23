import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock with Date")

window_width = 500
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="black")

frame = tk.Frame(root, bg="black", bd=10, relief="ridge")
frame.pack(padx=20, pady=20)

time_label = tk.Label(frame, font=("Segoe UI", 48, "bold"), bg="black", fg="#00FFFF")
time_label.pack()

date_label = tk.Label(frame, font=("Segoe UI", 20), bg="black", fg="white")
date_label.pack()

update_time()
root.mainloop()
