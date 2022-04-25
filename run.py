import quiz
from art import tprint
from datetime import datetime

now = datetime.now()

current_hour = int(now.strftime("%H"))


def pick_greeting(hour):
    if hour < 6:
        return "Wow, you're up late!"
    elif hour < 12:
        return "Good morning!"
    elif hour < 17:
        return "Good afternoon."
    else:
        return "Good evening."


greeting = pick_greeting(current_hour)


def main():
    """
    Code to run on terminal boot
    """

    tprint(" QUIZ\nMASTER\n 2022", font="o8")

    print(f"{greeting} Welcome to QuizMaster 2022! \n")

    # Prompt User to Set Up Quiz
    game_1 = quiz.setup_new_quiz()

    # Make a new quiz for testing purposes
    # game_1 = quiz.Game("Test Quiz", 5, 5, [9,23,24,25,26], "medium")

    print(game_1)
    print(game_1.describe())


main()
