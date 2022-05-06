from art import tprint
import os
from time import sleep
from termcolor import colored, cprint
import gdrive_utility
from helpers import ask_any_key, ask_yes_no, clear, current_hour
from create_gform import create_google_form
from create_quiz import *
from play_quiz import *

if os.path.exists("env.py"):
    import env  # noqa

# Password for Secret Google Drive Utility
SECRET = os.environ.get("ADMIN")


def pick_greeting(hour):
    """
    Returns a suitable greeting for the time of day.

    Args:
    hour: The current hour in 24hr time format
    """
    if hour < 6:
        return "Wow, you're up late!"
    elif hour < 11:
        return "Good morning!"
    elif hour < 17:
        return "Good afternoon,"
    else:
        return "Good evening,"


greeting = pick_greeting(current_hour)


def main():
    """
    Code to run on terminal boot
    """

    menu_options = ["(1) Play Quick Quiz Round",
                    "(2) Create Custom Quiz",
                    "(3) Create a Google Form Quiz",
                    "(4) Help"]

    help_text = ["""How to Use Quiz Master 2022 \n \n
    With Quiz Master 2022, you can create and play multiple choice quiz games
    either to play here in the terminal, or export as a Google Form that
    you can send to your friends - perfect for running an online table quiz!


    (1) Quick Quiz Round \n
    Play a short Quiz of 5 General Knowledge Questions here in the terminal.

    Chose an answer with the keys 1, 2, 3 or 4 and hit Enter.
    """,
                 """
    (2) Create Custom Quiz

    Choose custom settings such as categories, number of questions and
    difficulty and play here in the terminal.

    (3) Create a Google Form Quiz

    Choose custom settings, and then export your Quiz to a Google Form
    you can share with your friends.
    You can input your e-mail address and see the results as your friends
    submit their answers!

    Enter "Quit" or "Q" at any time to return to the Main Menu.

    See this project on GitHub at https://github.com/davidindub/quiz-master
    Quiz Master 2022 © David Kelly.
    """]

    clear()

    tprint(" QUIZ\nMASTER\n 2022", font="o8")

    cprint(f"{greeting} Welcome to Quiz Master 2022! \n", "green")
    sleep(2)

    while True:
        clear()

        # Main Menu:
        cprint("Main Menu", "white", "on_blue")
        print("_________\n")

        try:
            print("Please choose from the following:\n")

            for option in menu_options:
                print(option)

            response = int(
                input("\nPress Enter to confirm your selection. \n"))
        except ValueError:
            clear()
            continue

        if response == 1:
            # Creates a quiz round of 8 easy general knowledge questions
            quick_quiz = Game("Quick Quiz", 1, 8, [9], "easy")

            # Play the Quiz Game
            while True:
                play_terminal_quiz(quick_quiz)
                break

            continue

        if response == 2:
            # Prompts the user to set up their quiz
            custom_quiz = setup_new_quiz()

            # Play the Quiz the user just set up
            if custom_quiz:
                play_terminal_quiz(custom_quiz)

            continue
        if response == 3:
            print("OK you want to make a Google For Quiz"
                  " to share with friends")

            google_quiz = setup_new_quiz()

            try:
                create_google_form(google_quiz)
            except Exception:
                cprint("There was an error with the Google Form API\n\n", "red")
                print("Please try again later.")

            continue
        if response == 4:
            clear()
            tprint("HELP", font="o8")
            print(help_text[0])
            cprint("Press any key to read more.", "white", "on_blue")
            input()
            clear()
            print(help_text[1])
            ask_any_key()
            continue
        if response == 999:
            clear()
            cprint("\nGoogle Drive Utility Login", "blue")
            x = input("What is the password?\n")

            if x == SECRET:
                cprint("✅ Correct! Loading Google Drive Management...\n",
                       "green")
                sleep(1)
                clear()
                gdrive_utility.run()
                continue
            else:
                cprint("❌ Incorrect Password", "red")
                continue

        if response not in [1, 2, 3, 4, 999] or input == "":
            continue
        else:
            break


main()
