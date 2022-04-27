from os import system, name


def ask_yes_no(question):
    """
    Asks the user for input for a Yes/No Question
    and returns a boolean

    Args:
    question: The question to ask
    """
    yes = ["yes", "y"]
    no = ["no", "n"]
    done = False

    print(question)
    while not done:
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond [Y]es or [N]o")


def ask_any_key():
    input("Press any key to return to Main Menu.")
    return


def clear():
    """
    Clears the Terminal Window
    """
    # for Windows
    if name == 'nt':
        _ = system('cls')

    # for macOS/Linux
    else:
        _ = system('clear')