dummy_question = {'category': 'General Knowledge', 'type': 'multiple',
                  'difficulty': 'easy', 'question': 'Which sign of the zodiac comes between Virgo and Scorpio?',
                  'correct_answer': 'Libra',
                  'incorrect_answers': ['Gemini', 'Taurus', 'Capricorn']}


def create_gform_question(question_obj):
    """
    Takes a question python object and returns the JSON
    ready to use building the Google Form

    Args:
        question_obj: A Question object

    """
    return {
        "createItem": {
            "item": {
                "title": question_obj["question"],
                "questionItem": {
                    "question": {
                        "required": True,
                        "grading": {
                            "pointValue": 1,
                            "correctAnswers": {
                                "answers":
                                [{"value": question_obj["correct_answer"]}]
                            },
                        },
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                    {"value": question_obj["correct_answer"]},
                                    {"value": question_obj["incorrect_answers"][0]},
                                    {"value": question_obj["incorrect_answers"][1]},
                                    {"value": question_obj["incorrect_answers"][2]}
                            ],
                            "shuffle": True
                        }
                    }
                },
            },
            "location": {
                "index": 0
            }
        }
    }