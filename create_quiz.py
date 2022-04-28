from helpers import ask_any_key, ask_yes_no, clear
import requests
import json
import random
import sys
from termcolor import colored, cprint
from pprint import pprint
from time import sleep

CATEGORIES_DATA = json.loads(requests.get(
    "https://opentdb.com/api_category.php").text)["trivia_categories"]

SESSION_TOKEN = json.loads(requests.get(
    "https://opentdb.com/api_token.php?command=request").text)["token"]


def create_categories_dict(categories_data):
    """
    Creates a dictionary of quiz
    categories in the format id: category
    """
    cats_dict = {}

    for x in range(len(categories_data)):
        key, value = categories_data[x].values()
        cats_dict[key] = value

    return cats_dict


QUIZ_CATEGORIES = create_categories_dict(CATEGORIES_DATA)


def get_quiz_questions(num_qs, cat, diff):
    """
    Makes a call to the Quiz API and returns a list of
    multiple choice questions with category, type, difficulty,
    question, correct_answer and incorrect_answers
    """

    return json.loads(requests.get(
        f"https://opentdb.com/api.php?amount={num_qs}&category={cat}&difficulty={diff}&type=multiple&token={SESSION_TOKEN}").text)["results"]  # noqa


class Game:
    """
    Generates a Quiz Game,
    Expects 5 parameters: Quiz Title, Number of Rounds,
    Number of Questions in a round, a list of the categories
    for each round, and the difficulty
    """

    def __init__(self, quiz_title, num_rounds, num_qs, categories, difficulty):
        self.quiz_title = quiz_title
        self.num_rounds = num_rounds
        self.num_questions = num_qs
        self.categories = categories
        self.difficulty = difficulty

        self.rounds = [Round(x+1, self.num_questions, self.categories[x],
                             self.difficulty) for x in range(self.num_rounds)]

    def describe(self):
        cats_text = [QUIZ_CATEGORIES[cat] for cat in self.categories]

        print(f"Quiz title: {self.quiz_title}\n{self.num_rounds}"
              f" rounds of {self.num_questions} {self.difficulty} questions.\n"
              f"\n Categories are:\n")
        print(*cats_text, sep=", ")


class Round:
    """
    Generates a Quiz Round
    Expects four parameters: Round Number, Num of Questions,
    Category, and Difficulty
    """

    def __init__(self, round_num, num_qs, category, difficulty):

        self.round_num = round_num
        self.num_qs = num_qs
        self.category = category
        self.difficulty = difficulty

        self.question_data = get_quiz_questions(num_qs, category, difficulty)

        self.questions_list = [Question(**question)
                               for question in self.question_data]


class Question:
    """
    Creates a Quiz Question instance
    """

    def __init__(
        self, category, type, difficulty, question,
            correct_answer, incorrect_answers):

        self.category = category
        self.qtype = type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers


def setup_new_quiz():
    """
    Asks user for inputs and creates a new quiz based on the inputs
    """
    clear()

    while True:
        # Ask for the name of the Quiz
        while True:
            try:
                title = str(input("What is the name of your Quiz Game? \n"))
            except TypeError:
                continue
            if title == "":
                print("Please enter a name for the quiz. \n")
                continue
            else:
                break

        sleep(1)
        clear()

        # Ask how many round should the Quiz game have
        while True:
            try:
                rounds = int(input("How many rounds should the quiz have? \n"))
            except ValueError:
                cprint("You must enter a number of rounds for the quiz.\n",
                       "red")
                continue
            if rounds < 0:
                cprint("Sorry, you must enter a positive number.\n", "red")
                continue
            if rounds > 10:
                cprint("Sorry, you can only have a maximum of 10 rounds.",
                       "red")
                continue
            else:
                break

        sleep(1)
        clear()

        # Ask how many questions should be in each round
        while True:
            try:
                q_num = int(input("How many questions in each round? \n"))
            except ValueError:
                clear()
                print("You must enter a number of questions for each round.\n")
                continue
            if q_num < 0:
                clear()
                cprint("Sorry, you must enter a positive number\n", "red")
                continue
            if q_num > 5:
                cprint("Sorry, you can only have a max of 10"
                       "questions per round.", "red")
                continue
            else:
                break

        sleep(1)
        clear()

        # Print the list of Categories, ask what category
        # each round should be
        print_cats = ""
        for key in QUIZ_CATEGORIES:
            print_cats += f"{key}: {QUIZ_CATEGORIES[key]} \n"

        cats_selected = []
        for x in range(1, rounds+1):
            while True:
                try:
                    print("Available Categories:")
                    print(print_cats)
                    cat = int(input(f"Choose a category for Round {x}: \n"))
                except ValueError:
                    clear()
                    cprint(f"Please enter a valid category number from "
                           f"the list for round {x}. \n", "red")
                    continue
                if cat not in list(QUIZ_CATEGORIES):
                    clear()
                    cprint(f"Please enter a valid category number from "
                           f"the list for round {x}. \n", "red")
                    continue
                else:
                    cats_selected.append(cat)
                    clear()
                    break

        sleep(1)
        clear()

        # Ask what difficulty the questions should be
        while True:
            try:
                diff = input("What difficulty should the questions be? \n \n"
                             "Easy, Medium or Hard? \n").lower()
            except ValueError:
                continue
            if diff not in ["easy", "medium", "hard"]:
                continue
            else:
                break

        sleep(1)
        clear()

        game_obj = Game(title, rounds, q_num, cats_selected, diff)

        game_obj.describe()

        if ask_yes_no("Are these settings correct?"):
            return game_obj
        else:
            print("Okay, let's try again")
            sleep(1)
            clear()
            continue
