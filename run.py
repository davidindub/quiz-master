import quiz
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

    print(f"{greeting} Welcome to QuizMaster 2022! \n")

    game_1 = quiz.setup_new_quiz()

    print(game_1)


main()