import tkinter as tk
import pyautogui
import threading
import time

class AutoMouseApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("오토마우스")
        self.root.geometry("300x200")
        self.root.configure(bg="gray")

        self.start_button = tk.Button(self.root, text="시작", command=self.start_clicking)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(self.root, text="정지", command=self.stop_clicking)
        self.stop_button.pack(pady=20)

      self.clicking = False

def start_clicking(self):
        self.clicking = True
        self.click_thread = threading.Thread(target=self.auto_click)
        self.click_thread.start()

    def stop_clicking(self):
        self.clicking = False
        if self.click_thread.is_alive():
            self.click_thread.join()

    def auto_click(self):
        x, y = 100, 100
        while self.clicking:
            pyautogui.click(x, y)
            time.sleep(0.1)

def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AutoMouseApp()
    app.run()
