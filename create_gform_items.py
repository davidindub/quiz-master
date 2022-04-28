from create_quiz import QUIZ_CATEGORIES
TEST_QUESTION = {'category': 'General Knowledge', 'type': 'multiple',
                 'difficulty': 'easy', 'question': 'Which sign of the zodiac comes between Virgo and Scorpio?',
                 'correct_answer': 'Libra',
                 'incorrect_answers': ['Gemini', 'Taurus', 'Capricorn']}

TEST_ROUND = {'round_num': 1, 'num_qs': 5, 'category': 9, 'difficulty': 'medium',
              'question_data':
              [{'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                'question': 'Which essential condiment is also known as Japanese horseradish?',
                'correct_answer': 'Wasabi ',
                'incorrect_answers': ['Mentsuyu', 'Karashi', 'Ponzu']},
               {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                'question': 'What is the Swedish word for &quot;window&quot;?',
                  'correct_answer': 'F&ouml;nster',
                  'incorrect_answers': ['H&aring;l', 'Sk&auml;rm', 'Ruta']},
                  {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                   'question': 'Amsterdam Centraal station is twinned with what station?',
                   'correct_answer': 'London Liverpool Street',
                   'incorrect_answers': ['Frankfurt (Main) Hauptbahnhof', 'Paris Gare du Nord', 'Brussels Midi']},
                  {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                   'question': 'Computer manufacturer Compaq was acquired for $25 billion dollars in 2002 by which company?',
                   'correct_answer': 'Hewlett-Packard',
                   'incorrect_answers': ['Toshiba', 'Asus', 'Dell']},
                  {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                   'question': 'Which American manufactured submachine gun was informally known by the American soldiers that used it as &quot;Grease Gun&quot;?',
                   'correct_answer': 'M3', 'incorrect_answers': ['Colt 9mm', 'Thompson', 'MAC-10']}]}

TEST_GAME = {'quiz_title': 'Quick Quiz', 'num_rounds': 2, 'num_questions': 3, 'categories': [9, 9], 'difficulty': 'easy', 'rounds': [{'round_num': 1, 'num_qs': 5, 'category': 9, 'difficulty': 'medium',
                                                                                                                                      'question_data':
                                                                                                                                      [{'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                        'question': 'ROUND 1 Which essential condiment is also known as Japanese horseradish?',
                                                                                                                                        'correct_answer': 'Wasabi ',
                                                                                                                                        'incorrect_answers': ['Mentsuyu', 'Karashi', 'Ponzu']},
                                                                                                                                          {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                           'question': 'What is the Swedish word for &quot;window&quot;?',
                                                                                                                                           'correct_answer': 'F&ouml;nster',
                                                                                                                                           'incorrect_answers': ['H&aring;l', 'Sk&auml;rm', 'Ruta']},
                                                                                                                                          {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                           'question': 'Amsterdam Centraal station is twinned with what station?',
                                                                                                                                           'correct_answer': 'London Liverpool Street',
                                                                                                                                           'incorrect_answers': ['Frankfurt (Main) Hauptbahnhof', 'Paris Gare du Nord', 'Brussels Midi']},
                                                                                                                                          {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                           'question': 'Computer manufacturer Compaq was acquired for $25 billion dollars in 2002 by which company?',
                                                                                                                                           'correct_answer': 'Hewlett-Packard',
                                                                                                                                           'incorrect_answers': ['Toshiba', 'Asus', 'Dell']},
                                                                                                                                          {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                           'question': 'Which American manufactured submachine gun was informally known by the American soldiers that used it as &quot;Grease Gun&quot;?',
                                                                                                                                           'correct_answer': 'M3', 'incorrect_answers': ['Colt 9mm', 'Thompson', 'MAC-10']}]},

                                                                                                                                     {'round_num': 2, 'num_qs': 5, 'category': 9, 'difficulty': 'medium',
                                                                                                                                      'question_data':
                                                                                                                                      [{'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                        'question': 'ROUND 2 Which essential condiment is also known as Japanese horseradish?',
                                                                                                                                        'correct_answer': 'Wasabi ',
                                                                                                                                        'incorrect_answers': ['Mentsuyu', 'Karashi', 'Ponzu']},
                                                                                                                                          {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                           'question': 'What is the Swedish word for &quot;window&quot;?',
                                                                                                                                           'correct_answer': 'F&ouml;nster',
                                                                                                                                           'incorrect_answers': ['H&aring;l', 'Sk&auml;rm', 'Ruta']},
                                                                                                                                          {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                           'question': 'Amsterdam Centraal station is twinned with what station?',
                                                                                                                                           'correct_answer': 'London Liverpool Street',
                                                                                                                                           'incorrect_answers': ['Frankfurt (Main) Hauptbahnhof', 'Paris Gare du Nord', 'Brussels Midi']},
                                                                                                                                          {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                           'question': 'Computer manufacturer Compaq was acquired for $25 billion dollars in 2002 by which company?',
                                                                                                                                           'correct_answer': 'Hewlett-Packard',
                                                                                                                                           'incorrect_answers': ['Toshiba', 'Asus', 'Dell']},
                                                                                                                                          {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                           'question': 'Which American manufactured submachine gun was informally known by the American soldiers that used it as &quot;Grease Gun&quot;?',
                                                                                                                                           'correct_answer': 'M3', 'incorrect_answers': ['Colt 9mm', 'Thompson', 'MAC-10']}]},

                                                                                                                                     {'round_num': 3, 'num_qs': 5, 'category': 9, 'difficulty': 'medium',
                                                                                                                                      'question_data':
                                                                                                                                      [{'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                        'question': 'ROUND 3 Which essential condiment is also known as Japanese horseradish?',
                                                                                                                                        'correct_answer': 'Wasabi ',
                                                                                                                                        'incorrect_answers': ['Mentsuyu', 'Karashi', 'Ponzu']},
                                                                                                                                       {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                        'question': 'What is the Swedish word for &quot;window&quot;?',
                                                                                                                                           'correct_answer': 'F&ouml;nster',
                                                                                                                                           'incorrect_answers': ['H&aring;l', 'Sk&auml;rm', 'Ruta']},
                                                                                                                                       {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                        'question': 'Amsterdam Centraal station is twinned with what station?',
                                                                                                                                           'correct_answer': 'London Liverpool Street',
                                                                                                                                           'incorrect_answers': ['Frankfurt (Main) Hauptbahnhof', 'Paris Gare du Nord', 'Brussels Midi']},
                                                                                                                                       {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                        'question': 'Computer manufacturer Compaq was acquired for $25 billion dollars in 2002 by which company?',
                                                                                                                                           'correct_answer': 'Hewlett-Packard',
                                                                                                                                           'incorrect_answers': ['Toshiba', 'Asus', 'Dell']},
                                                                                                                                       {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'medium',
                                                                                                                                        'question': 'Which American manufactured submachine gun was informally known by the American soldiers that used it as &quot;Grease Gun&quot;?',
                                                                                                                                           'correct_answer': 'M3', 'incorrect_answers': ['Colt 9mm', 'Thompson', 'MAC-10']}]}
                                                                                                                                     ]}


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
                                    {"value":
                                     question_obj["correct_answer"]},
                                    {"value":
                                     question_obj["incorrect_answers"][0]},
                                    {"value":
                                     question_obj["incorrect_answers"][1]},
                                    {"value":
                                     question_obj["incorrect_answers"][2]}
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


def create_gform_text_question(question_to_ask):
    """
    Makes a Google Forms questions with a
    text field input for response

    Args:
    question_to_ask: The Question to ask
    """
    return {
        "createItem": {
            "item": {
                "title": question_to_ask,
                "questionItem": {
                    "question": {
                        "required": True,
                        "textQuestion": {
                            "paragraph": False
                        }
                    },
                },
            },
            "location": {
                "index": 0
            }
        }
    }


def create_gform_page_break(round_num, category):
    """
    Creates a page break for a Google Form

    Args:
    round_num: The number of the round
    category: The index of the category of the round
    """
    page_break = {
        "createItem": {
            "item": {
                "title": f"Round {round_num}: {QUIZ_CATEGORIES[category]}",
                "pageBreakItem": {}
            },
            "location": {
                "index": 0
            }
        },
    }

    return page_break


def create_gform_round(round_obj):
    """
    Takes a game round python object and returns a list
    of 'createItem' objects to send to the Google Forms
    API

    Args:
        round_obj: A Round object
    """
    round_obj = round_obj.__dict__

    nums_qs = round_obj["num_qs"]
    round_num = round_obj["round_num"]
    category = round_obj["category"]
    questions = round_obj["question_data"]
    form_items = []

    for question in questions:
        form_items.insert(0, create_gform_question(question))

    form_items.append(create_gform_page_break(round_num, category))

    return form_items


def create_gform_game(game_obj):
    """
    Takes a quiz game python object and returns a list
    of 'createItem' objects to send to the Google Forms
    API

    Args:
        game_obj: A Quiz Game object
    """

    form_items = []
    rounds = game_obj.rounds

    for round in rounds:
        form_items.insert(0, create_gform_round(round))

    return form_items

