import create_quiz
import play_quiz
from art import tprint
from datetime import datetime
from os import system, name

now = datetime.now()

current_hour = int(now.strftime("%H"))


def pick_greeting(hour):
    """
    Returns a suitable greeting for the time of day.

    Args:
    hour: The current hour in 24hr time format
    """
    if hour < 6:
        return "Wow, you're up late!"
    elif hour < 12:
        return "Good morning!"
    elif hour < 17:
        return "Good afternoon."
    else:
        return "Good evening."


def clear():
    """
    Clears the Terminal Window
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


greeting = pick_greeting(current_hour)


def main():
    """
    Code to run on terminal boot
    """

    tprint(" QUIZ\nMASTER\n 2022", font="o8")

    print(f"{greeting} Welcome to Quiz Master 2022! \n")

    # Prompt User to Set Up Quiz
    # game_1 = quiz.setup_new_quiz()

    # Make a new quiz for testing purposes
    # game_1 = quiz.Game("Test Quiz", 5, 5, [9,23,24,25,26], "medium")

    # print(game_1)
    # print(game_1.describe())

    # sleep(1)
    # clear()

    # Main Menu:
    print("Quiz Master 2002 Main Menu")
    print("\n##########################\n")

    menu_options = ["(1) Play Quick Quiz Round",
                    "(2) Create Custom Quiz",
                    "(3) Create a quiz round to share",
                    "(4) How to Use Quiz Master"]

    while True:
        try:
            print("Please choose from the following:")

            for option in menu_options:
                print(option)

            response = int(input("What would you like to do? \n"))
        except ValueError:
            clear()
            continue

        if response == 1:
            print("OK you want a quick quiz!")
            
            # Creates a quiz round of 8 easy general knowledge questions
            quick_quiz = create_quiz.Game("Quick Quiz", 1, 2, [9], "easy")

            quick_quiz.describe()

            play_quiz.play_terminal_quiz(quick_quiz)

            break

        if response == 2:
            print("OK you want to make a custom Quiz!")

            # Prompts the user to set up their quiz
            custom_quiz = create_quiz.setup_new_quiz()

            play_quiz.play_terminal_quiz(custom_quiz)

            break
        if response == 3:
            print("OK you want to make a Google For Quiz to share with friends")
            break
        if response == 4:
            print("OK you want the help screen")
            break
        if response not in [1, 2, 3, 4] or input == "":
            continue
        else:
            break


main()
