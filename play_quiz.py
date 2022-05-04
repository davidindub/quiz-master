import random
from time import sleep
from art import tprint
from helpers import clear, ask_any_key, is_quit
from create_quiz import QUIZ_CATEGORIES


def play_terminal_quiz(game_obj):
    """
    Runs a quiz game in the terminal

    Args:
    game_obj: A Quiz game object
    """
    GAME = game_obj
    NUM_ROUNDS = GAME.num_rounds
    TOTAL_NUM_QS = GAME.num_rounds * GAME.num_questions
    total_score = 0

    for round in GAME.rounds:
        round_score = 0

        clear()
        print(
            f"Round {round.round_num}: {QUIZ_CATEGORIES[round.category]}")
        sleep(2)

        for question in round.questions_list:

            all_answers = (question.incorrect_answers +
                            [question.correct_answer])

            # Shuffle the Answers
            random.shuffle(all_answers)

            # Check the index of the correct answer, add 1 to match input
            expected_answer = (all_answers.index(
                question.correct_answer)) + 1

            while True:
                try:
                    sleep(1)
                    clear()
                    print(question.question)

                    for x in range(len(all_answers)):
                        print(f"({x+1}) {all_answers[x]}")

                    answer = input("\n Answer: \n")

                    if is_quit(answer):
                        return

                    answer = int(answer)

                except ValueError:
                    print("Please enter an answer 1, 2, 3 or 4")
                    continue
                if answer == expected_answer:
                    print("\n ✅ Correct! ✅ \n")
                    round_score += 1
                    break
                if answer not in [1, 2, 3, 4]:
                    print("Please enter an answer 1, 2, 3 or 4")
                    continue
                else:
                    print("\n ❌ Wrong! ❌ \n")
                    break

        total_score += round_score
        print(f"Round {round.round_num} over!")
        print(f"You got {round_score} / {round.num_qs} correct "
                f"in Round {round.round_num}.")
        sleep(2)

    clear()
    tprint(f"QUIZ\nOVER!", font="o8")
    print(f"\n Calculating your results............\n")
    sleep(1)
    print(f".......................................\n")
    sleep(1)
    print(
        f"You got a total of {total_score} / {TOTAL_NUM_QS} questions correct.\n")
    sleep(1)

    ask_any_key()
    return
