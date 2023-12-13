from questionary import questionary
import time
import webbrowser
import threading


def select_study_area():
    """Select the study area."""
    selected_area = questionary.select(
        "Select Study Area",
        choices=["1.응예공", "2.오픈소스", "3.객프", "4.콘수", "5.기타"],
    ).ask()
    print(f"You selected: {selected_area}")
    return selected_area


def confirm_study_preparation():
    """Confirm if user is ready to study."""
    ready_to_study = questionary.confirm("Are you ready to start studying?").ask()
    if ready_to_study:
        print("Great! Let's get started.")
    else:
        print("Okay, take your time and start when you are ready.")
    return ready_to_study


def time_elapsed():
    """Function to be called at regular intervals to update the timer."""
    global time_thread, time_set

    time_set[0] -= 1
    time_set[1] += 1

    if time_set[0] <= 0:
        time_thread.cancel()
        print("Time's up!")
        webbrowser.open("https://youtu.be/rmtNOh6GJW8?si=XCm-wIXWxoysCKQR")
        return

    print(f"Time Remaining: {time_set[0] // 60} minutes {time_set[0] % 60} seconds")
    time_thread = threading.Timer(1, time_elapsed)
    time_thread.start()


def start_timer():
    """Start the timer based on user input."""
    global time_set, time_thread

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
    print("Welcome to the Study Timer App")

    # Study area selection
    selected_area = select_study_area()

    # Confirmation for study preparation
    study_preparation_confirmed = confirm_study_preparation()

    if study_preparation_confirmed:
        # If the user is ready to study, start the timer
        print("Time Timer")
        start = input("Press Enter to start the timer")
        start_timer()
    else:
        print("Okay, you can start the timer later.")
from questionary import questionary
import time
import webbrowser
import threading


def select_study_area():
    """Select the study area."""
    selected_area = questionary.select(
        "Select Study Area",
        choices=["1.응예공", "2.오픈소스", "3.객프", "4.콘수", "5.기타"],
    ).ask()
    print(f"You selected: {selected_area}")
    return selected_area


def confirm_study_preparation():
    """Confirm if user is ready to study."""
    ready_to_study = questionary.confirm("Are you ready to start studying?").ask()
    if ready_to_study:
        print("Great! Let's get started.")
    else:
        print("Okay, take your time and start when you are ready.")
    return ready_to_study


def time_elapsed():
    """Function to be called at regular intervals to update the timer."""
    global time_thread, time_set

    time_set[0] -= 1
    time_set[1] += 1

    if time_set[0] <= 0:
        time_thread.cancel()
        print("Time's up!")
        webbrowser.open("https://youtu.be/rmtNOh6GJW8?si=XCm-wIXWxoysCKQR")
        return

    print(f"Time Remaining: {time_set[0] // 60} minutes {time_set[0] % 60} seconds")
    time_thread = threading.Timer(1, time_elapsed)
    time_thread.start()

def start_timer():
    """Start the timer based on user input."""
    global time_set, time_thread

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
    print("Welcome to the Study Timer App")

    # Study area selection
    selected_area = select_study_area()

    # Confirmation for study preparation
    study_preparation_confirmed = confirm_study_preparation()

    if study_preparation_confirmed:
        # If the user is ready to study, start the timer
        print("Time Timer")
        start = input("Press Enter to start the timer")
        start_timer()
    else:
        print("Okay, you can start the timer later.")

def ask_exit():
    """Ask the user if they want to exit the application."""
    exit_choice = input("Do you want to exit? (y/n): ").lower()
    return exit_choice == 'y'


if __name__ == '__main__':
    print("Welcome to the Study Timer App")

    while True:
        # Study area selection
        selected_area = select_study_area()

        # Confirmation for study preparation
        study_preparation_confirmed = confirm_study_preparation()

        if study_preparation_confirmed:
            # If the user is ready to study, start the timer
            print("Time Timer")
            start = input("Press Enter to start the timer")
            start_timer()

            while True:
                if time_thread.is_alive():
                    exit_choice = input("Do you want to stop the timer and exit? (y/n): ").lower()
                    if exit_choice == 'y':
                        time_thread.cancel()
                        break
                else:
                    restart_choice = input("Timer has finished. Do you want to restart? (y/n): ").lower()
                    if restart_choice == 'y':
                        break
                    elif restart_choice == 'n':
                        exit()

        else:
            print("Okay, you can start the timer later.")

        if ask_exit():
            break


