import time
import webbrowser
import threading
from tkinter import Tk, Label, Button, StringVar, OptionMenu

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Timer")

        self.selected_area = StringVar()
        self.selected_area.set("1.응예공")  # Default value

        Label(root, text="선택한 영역").pack()
        OptionMenu(root, self.selected_area, "1.응예공", "2.오픈소스", "3.객프", "4.콘수", "5.기타").pack()

        Button(root, text="시작", command=self.start_timer).pack()

        self.timer_label = Label(root, text="")
        self.timer_label.pack()

    def start_timer(self):
        selected_area = self.selected_area.get()
        print(f"Selected Area: {selected_area}")

        if not questionary.confirm("공부할 준비가 되었습니까?").ask():
            return

        input_time = questionary.text("Insert time to check (in minutes):").ask()
        try:
            input_time = int(input_time)
        except ValueError:
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
            print("Time's up!")
            webbrowser.open("https://youtu.be/rmtNOh6GJW8?si=XCm-wIXWxoysCKQR")
            return 0

        time_str = f"Time Remaining: {self.time_set[0] // 60} minutes {self.time_set[0] % 60} seconds"
        self.timer_label.config(text=time_str)

        self.time_thread = threading.Timer(1, self.time_elapsed)
        self.time_thread.start()

if __name__ == "__main__":
    root = Tk()
    app = TimerApp(root)
    root.mainloop()

