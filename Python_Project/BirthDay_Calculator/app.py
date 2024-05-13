import tkinter as tk
from tkinter import messagebox
import datetime

def calculate_days_until_birthday():
    month = int(month_entry.get())
    day = int(day_entry.get())

    birthday = datetime.datetime(2023, month, day)
    today = datetime.datetime.now()

    days_until_birthday = (birthday - today).days

    if days_until_birthday < 0:
        birthday = datetime.datetime(2024, month, day)
        days_until_birthday = (birthday - today).days

    messagebox.showinfo("Days Until Birthday", f"생일은 {abs(days_until_birthday)}일 남았습니다.")

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("Birthday Calculator")

tk.Label(window, text="생일 월").grid(row=0, column=0)
month_entry = tk.Entry(window)
month_entry.grid(row=0, column=1)

tk.Label(window, text="생일 일").grid(row=1, column=0)
day_entry = tk.Entry(window)
day_entry.grid(row=1, column=1)

calculate_button = tk.Button(window, text="계산", command=calculate_days_until_birthday)
calculate_button.grid(row=2, columnspan=2)

window.mainloop()
