import random

def play_terminal_quiz(game_obj):
    """
    Runs a quiz game in the terminal

    Args:
    game_obj: A Quiz game object
    """
    GAME = game_obj

    for round in GAME.rounds:
        round_score = 0

        for question in round.questions_list:

            all_answers = (question.incorrect_answers +
                           [question.correct_answer])
            
            random.shuffle(all_answers)

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
                    print("✅ Well done! ✅")
                    round_score += 1
                    break
                else:
                    print("❌ Wrong! ❌")
                    break
        
        print(f"You got {round_score} / {round.num_qs} correct!")
