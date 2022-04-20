import requests
import json
import random
from pprint import pprint

categories = json.loads(requests.get(
    "https://opentdb.com/api_category.php").text)["trivia_categories"]


def get_quiz_questions(num_qs, cat, diff):
    """
    Makes a call to the Quiz API and returns a list of
    multiple choice questions with category, type, difficulty,
    question, correct_answer and incorrect_answers
    """
    return json.loads(requests.get(
        f"https://opentdb.com/api.php?amount={num_qs}&category={cat}&difficulty={diff}&type=multiple").text)["results"]


class Game:
    """
    Generates a Quiz Game of several Rounds
    """

    def __init__(self, quiz_title, num_rounds):
        self.quiz_title = quiz_title
        self.num_rounds = num_rounds


class Round:
    """
    Generates a Quiz Round
    Expects three parameters: Num of Questions,
    Category, and Difficulty
    """

    def __init__(self, num_qs, category, difficulty):

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

    def __init__(self, category, type, difficulty, question, correct_answer, incorrect_answers):

        self.category = category
        self.qtype = type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

    def ask(self):
        return self.question


def get_quiz_categories(categories):

    print_cats = ""
    for x in range(len(categories)):
        print_cats += (f"{categories[x]['id']}: {categories[x]['name']} \n")

    return print_cats


def main():

    print("Welcome to QuizMaster 2022! \n")

    round_1 = Round(5, 9, "easy")


main()
