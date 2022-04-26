import random
from time import sleep


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

        for question in round.questions_list:

            all_answers = (question.incorrect_answers +
                           [question.correct_answer])
            
            # Shuffle the Answers
            random.shuffle(all_answers)

            # Check the index of the correct answer, add 1 to match user input
            expected_answer = (all_answers.index(question.correct_answer)) + 1

            while True:
                try:
                    print(question.question)

                    for answer in all_answers:
                        print(answer)

                    answer = int(input("Answer: \n"))
                except ValueError:
                    print("Please enter an answer 1, 2, 3 or 4")
                    continue
                if answer == expected_answer:
                    print("✅ Correct! ✅")
                    round_score += 1
                    sleep(1)
                    break
                if answer not in [1, 2, 3, 4]:
                    print("Please enter an answer 1, 2, 3 or 4")
                    continue
                else:
                    print("❌ Wrong! ❌")
                    sleep(1)
                    break
        
        total_score += round_score
        print(f"Round {round.round_num} over!")
        print(f"You got {round_score} / {round.num_qs} correct!")

    print(f"Quiz over! Calculating your results............")
    sleep(1)
    print(f"...............................................")
    sleep(1)
    print(f"You got {total_score} / {TOTAL_NUM_QS} questions correct.")

