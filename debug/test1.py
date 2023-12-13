import tkinter as tk
from tkinter import ttk
import webbrowser
import threading

class StudyTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("공부 타이머 앱")

        self.selected_area = tk.StringVar()
        self.selected_area.set("1.응예공")  # Default value

        ttk.Label(root, text="선택한 영역").pack()
        ttk.Combobox(root, textvariable=self.selected_area, values=["1.응예공", "2.오픈소스", "3.객프", "4.콘수", "5.기타"]).pack()

        ttk.Button(root, text="공부 시작", command=self.start_study).pack()

        self.timer_label = ttk.Label(root, text="")
        self.timer_label.pack()

        self.time_set = []
        self.time_thread = None

    def start_study(self):
        selected_area = self.selected_area.get()
        print(f"Selected Area: {selected_area}")

        if not self.ask_ok_cancel("공부 준비", "공부할 준비가 되었습니까?"):
            return

        input_time = self.ask_integer("시간 설정", "공부할 시간을 입력하세요(분):", minvalue=1)
        if input_time is None:
            input_time = 1

        self.start_time = input_time * 60
        self.time_set = [self.start_time, self.start_time]

        self.time_thread = threading.Timer(1, self.time_elapsed)
        self.time_thread.start()

    def time_elapsed(self):
        self.time_set[0] = self.time_set[0] - 1
        self.time_set[1] = self.time_set[1] + 1

        if self.time_set[0] <= 0:
            self.time_thread.cancel()
            print("시간 종료!")
            self.show_info("공부 타이머", "시간 종료!\n휴식을 취하세요!")
            webbrowser.open("https://youtu.be/rmtNOh6GJW8?si=XCm-wIXWxoysCKQR")
            return

        time_str = f"남은 시간: {self.time_set[0] // 60}분 {self.time_set[0] % 60}초"
        self.timer_label.config(text=time_str)

        self.time_thread = threading.Timer(1, self.time_elapsed)
        self.time_thread.start()

    def ask_ok_cancel(self, title, message):
        return tk.messagebox.askokcancel(title, message)

    def ask_integer(self, title, message, minvalue=0):
        return tk.simpledialog.askinteger(title, message, minvalue=minvalue)

    def show_info(self, title, message):
        tk.messagebox.showinfo(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimerApp(root)
    root.mainloop()

