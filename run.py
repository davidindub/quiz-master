from art import tprint
from datetime import datetime
from os import system, name
from time import sleep
import sys
from termcolor import colored, cprint
from helpers import ask_any_key, ask_yes_no, clear
import create_quiz
import play_quiz
import create_form

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
    \n \n
    (1) Quick Quiz Round \n
    Play a short Quiz of 5 General Knowledge Questions here in the terminal.

    Chose an answer with the keys 1, 2, 3 or 4 and hit Enter.
    """,
    """
    (2) Create Custom Quiz \n
    Choose custom settings such as categories, number of questions and
    difficulty and play here in the terminal.
    \n \n
    (3) Create a Google Form Quiz \n
    Choose custom settings, and then export your Quiz to a Google Form
    you can share with your friends.
    You can input your e-mail address and see the results as your friends
    submit their answers!
    \n \n
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
        print("Main Menu")
        print("\n##########################\n")

        try:
            print("Please choose from the following:\n")

            for option in menu_options:
                print(option)

            response = int(input("\nPress Enter to confirm your selection \n"))
        except ValueError:
            clear()
            continue

        if response == 1:
            # Creates a quiz round of 8 easy general knowledge questions
            quick_quiz = create_quiz.Game("Quick Quiz", 1, 8, [9], "easy")
            print(quick_quiz.__dict__)

            # Play the Quiz Game
            play_quiz.play_terminal_quiz(quick_quiz)

            continue

        if response == 2:
            print("OK you want to make a custom Quiz!")

            # Prompts the user to set up their quiz
            custom_quiz = create_quiz.setup_new_quiz()

            # Play the Quiz the user just set up
            play_quiz.play_terminal_quiz(custom_quiz)

            continue
        if response == 3:
            print("OK you want to make a Google For Quiz to share with friends")

            google_quiz = create_quiz.setup_new_quiz()

            create_form.create_google_form(google_quiz)

            break
        if response == 4:
            clear()
            tprint("HELP", font="o8")
            print(help_text[0])
            input("Press any key to read more.\n")
            clear()
            print(help_text[1])
            ask_any_key()
            continue
        if response not in [1, 2, 3, 4] or input == "":
            continue
        else:
            break


main()
