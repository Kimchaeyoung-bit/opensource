from questionary import questionary
import time
import webbrowser
import threading
import msvcrt

time_set = [0, 0]
time_thread = None

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

def confirm_open_wikipedia(selected_area):
    """Ask the user if they want to open the Wikipedia page for the selected area."""
    open_wikipedia = questionary.confirm(f"Do you want to open the Wikipedia page for {selected_area}?").ask()
    return open_wikipedia

def time_elapsed():
    """Function to be called at regular intervals to update the timer."""
    global time_set, time_thread

    time_set[0] -= 1
    time_set[1] += 1

    if time_set[0] <= 0:
        print("Time's up!")
        open_wikipedia_page(selected_area)
        return

    print(f"Time Remaining: {time_set[0] // 60} minutes {time_set[0] % 60} seconds")
    time_thread = threading.Timer(1, time_elapsed)
    time_thread.start()

def open_wikipedia_page(selected_area):
    """Open the Wikipedia page based on the selected study area."""
    wikipedia_pages = {
        "1.응예공": "https://ko.wikipedia.org/wiki/응용_공학",
        "2.오픈소스": "https://ko.wikipedia.org/wiki/오픈_소스",
        "3.객프": "https://ko.wikipedia.org/wiki/객체_지향_프로그래밍",
        "4.콘수": "https://ko.wikipedia.org/wiki/컴퓨터_구조",
        "5.기타": "https://ko.wikipedia.org/wiki/기타",
    }

    selected_page = wikipedia_pages.get(selected_area)
    if selected_page:
        open_wikipedia = confirm_open_wikipedia(selected_area)
        if open_wikipedia:
            webbrowser.open(selected_page)
            print(f"Opening Wikipedia page for {selected_area}")
    else:
        print("No Wikipedia page available for the selected area.")

def start_timer(input_time):
    """Start the timer based on user input."""
    global time_set, time_thread

    start_time = input_time * 60
    time_set = [start_time, start_time]

    time_thread = threading.Timer(1, time_elapsed)
    time_thread.start()

def start_or_restart():
    """Ask the user if they want to restart or exit."""

    while True:
        print("Do you want to restart? (y/n): ", end="", flush=True)
        restart_choice = msvcrt.getch().decode().lower()
        print(restart_choice)
        if restart_choice in ['y', 'n']:
            print()
            return restart_choice == 'y'

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
            try:
                input_time = int(input("Insert time to check (in minutes): "))
            except ValueError:
                input_time = 1

            start_timer(input_time)

            # Wait for the timer to finish
            time_thread.join()

            # Ask if the user wants to restart
            if start_or_restart():
                # If restarting, reset study preparation confirmation
                study_preparation_confirmed = False
                time_thread.cancel()  # Cancel the existing timer thread
            else:
                # If not restarting, exit the loop
                break

        else:
            print("Okay, you can start the timer later.")

        # Ask if the user wants to exit
        print("Do you want to exit? (y/n): ", end="", flush=True)
        exit_choice = msvcrt.getch().decode().lower()
        print(exit_choice)
        

