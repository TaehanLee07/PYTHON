import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    letter = ""

    # 비밀번호에 어떤 문자가 들어가야 하는지 확인
    types = [upper_case_var.get(), lower_case_var.get(), digits_var.get(), punctuation_var.get()]

    rChar = ""
    if types[0]:
        rChar += string.ascii_uppercase
    
    if types[1]:
        rChar += string.ascii_lowercase
    
    if types[2]:
        rChar += string.digits
    
    if types[3]:
        rChar += string.punctuation

    length = int(length_entry.get())

    # 무작위로 비밀번호 생성
    for _ in range(length):
        letter += random.choice(rChar)

    password_var.set(letter)

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("Password Generator")

# 레이블 생성
tk.Label(window, text="비밀번호 길이").grid(row=0, column=0)
tk.Label(window, text="비밀번호 구성 요소").grid(row=1, column=0)
tk.Label(window, text="생성된 비밀번호").grid(row=2, column=0)

# 입력 필드 생성
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)

# 체크박스 생성
upper_case_var = tk.BooleanVar()
lower_case_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
punctuation_var = tk.BooleanVar()

tk.Checkbutton(window, text="영문 대문자", variable=upper_case_var).grid(row=1, column=1, sticky="w")
tk.Checkbutton(window, text="영문 소문자", variable=lower_case_var).grid(row=1, column=1, sticky="w", pady=20)
tk.Checkbutton(window, text="숫자", variable=digits_var).grid(row=1, column=1, sticky="w", pady=40)
tk.Checkbutton(window, text="특수 문자", variable=punctuation_var).grid(row=1, column=1, sticky="w", pady=80)

# 비밀번호 생성 버튼 생성
generate_button = tk.Button(window, text="생성", command=generate_password)
generate_button.grid(row=1, column=2)

# 생성된 비밀번호 출력 필드 생성
password_var = tk.StringVar()
password_entry = tk.Entry(window, textvariable=password_var, state='readonly')
password_entry.grid(row=2, column=1)

# Tkinter 윈도우 실행
window.mainloop()
