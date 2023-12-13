import questionary
import time
import webbrowser
import threading
import os
import openai


time_set = [0, 0]
time_thread = None
is_timer_running = False
paused_time = 0

def select_study_area():
    """스터디 영역 선택."""
    selected_area = questionary.select(
        "스터디 영역을 선택하세요",
        choices=["1.응예공", "2.오픈소스", "3.객프", "4.콘수", "5.기타"],
    ).ask()
    print(f"선택한 영역: {selected_area}")
    return selected_area

openai.api_key ="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"
question = input("공부할 과목과 분량을 적어주세요 : ")

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": question}
        ]
    )

print(completion.choices[0].message.content)


def confirm_study_preparation():
    """사용자가 공부 준비를 완료했는지 확인."""
    ready_to_study = questionary.confirm("공부를 시작할 준비가 되셨나요?").ask()
    if ready_to_study:
        print("좋아요! 시작합시다.")
    else:
        print("알겠습니다. 준비가 되면 시작하세요.")
    return ready_to_study

def time_elapsed():
    """타이머를 업데이트하기 위해 정기적으로 호출되는 함수."""
    global time_set, time_thread, paused_time

    time_set[0] -= 1
    time_set[1] += 1

    if time_set[0] <= 0:
        print("시간 종료!")
        webbrowser.open("https://youtu.be/_JsemaQu-5w?feature=shared")
        return

    print(f"남은 시간: {time_set[0] // 60} 분 {time_set[0] % 60} 초")

    if is_timer_running:
        time_thread = threading.Timer(1, time_elapsed)
        time_thread.start()

def start_timer(input_time):
    """사용자 입력에 기반하여 타이머 시작."""
    global time_set, time_thread, is_timer_running, paused_time

    start_time = input_time * 60
    time_set = [start_time, start_time]
    is_timer_running = True

    time_thread = threading.Timer(1, time_elapsed)
    time_thread.start()

def stop_timer():
    """타이머 정지."""
    global is_timer_running, time_thread, paused_time
    if is_timer_running:
        is_timer_running = False
        time_thread.cancel()
        paused_time = time_set[0]

def resume_timer():
    """타이머 재개."""
    global is_timer_running, time_thread, paused_time
    if not is_timer_running:
        is_timer_running = True
        time_set[0] = paused_time
        time_thread = threading.Timer(1, time_elapsed)
        time_thread.start()

if __name__ == '__main__':
    print("Study Timer App에 오신 것을 환영합니다")

    while True:
        # 스터디 영역 선택
        selected_area = select_study_area()

        # 공부 준비 확인
        study_preparation_confirmed = confirm_study_preparation()

        if study_preparation_confirmed:
            # 사용자가 공부 준비가 되었으면 타이머 시작
            print("타이머 시작")
            try:
                input_time = int(input("확인할 시간을 입력하세요 (분): "))
            except ValueError:
                input_time = 1

            start_timer(input_time)

            # 사용자가 프로그램을 중지하거나 재개할 수 있도록 함
            while is_timer_running:
                user_choice = input("타이머를 중지하려면 's'를 입력하세요: ").lower()
                
                if user_choice == 's':
                    stop_timer()

            # 사용자에게 재시작 여부 묻기
            restart_choice = input("재시작하시겠습니까? (y/n): ").lower()
            if restart_choice != 'y':
                break

        else:
            print("알겠습니다. 나중에 타이머를 시작하세요.")

        # 사용자가 종료할지 묻기
        exit_choice = input("종료하시겠습니까? (y/n): ").lower()
        if exit_choice == 'y':
            break
