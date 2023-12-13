
from questionary import questionary
import time
import webbrowser
import threading


questionary.select(
    "선택한 영역",
    choices=["1.응예공", "2.오픈소스", "3.객프", "4.콘수", "5.기타"],
).ask()

questionary.confirm("공부할 준비가 되었습니까?").ask()


global time_set
global time_thread

def time_elapsed():
    global time_thread
    global time_set

    time_set[0] = time_set[0] - 1
    time_set[1] = time_set[1] + 1

    if time_set[0] <= 0:
        time_thread.cancel()
        print("Time's up!")
        webbrowser.open("https://youtu.be/rmtNOh6GJW8?si=XCm-wIXWxoysCKQR")
        return 0

    print(f"Time Remaining: {time_set[0] // 60} minutes {time_set[0] % 60} seconds")
    time_thread = threading.Timer(1, time_elapsed)
    time_thread.start()

def time_start(val):
    global time_set
    global time_thread

    try:
        input_time = int(input("Insert time to check (in minutes): "))
    except ValueError:
        input_time = 1

    start_time = input_time * 60
    time_set = [start_time, start_time]

    try:
        time_thread.cancel()
    except:
        pass

    time_thread = threading.Timer(1, time_elapsed)
    time_thread.start()

if __name__ == '__main__':
    print("Time Timer")
    start = input("Press Enter to start the timer")
    time_start(None)


