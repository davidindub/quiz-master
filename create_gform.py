from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from apiclient import discovery, errors
from email_validator import validate_email, EmailNotValidError
from helpers import ask_yes_no, is_quit, now, clear, ask_any_key
from termcolor import cprint
from gdrive_utility import insert_permission, DRIVE_SERVICE
from create_gform_items import (
    create_gform_question, create_gform_round,
    create_gform_text_question, create_gform_game)


CREDS = service_account.Credentials.from_service_account_file("creds.json")

SCOPED_CREDENTIALS = CREDS.with_scopes(
    ["https://www.googleapis.com/auth/forms.body"])

DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

FORM_SERVICE = discovery.build("forms", "v1", credentials=SCOPED_CREDENTIALS,
                               discoveryServiceUrl=DISCOVERY_DOC,
                               static_discovery=False)

# End of Authorisation Code


def create_gform_body(game_obj):
    """
    Returns the request body to send to the Google Forms
    API for a new Quiz Game

    Args:
    game_obj: A Quiz Game Object
    """

    form_questions = create_gform_game(game_obj)
    todays_date = now.strftime("%x")

    body = {
        "requests": [
            {
                "updateSettings": {
                    "settings": {
                        "quizSettings": {
                            "isQuiz": True
                        }
                    },
                    "updateMask": "quizSettings.isQuiz"
                }
            },
            {
                "updateFormInfo": {
                    "info": {
                        "title": game_obj.quiz_title,
                        "documentTitle": game_obj.quiz_title,
                        "description": f"This quiz was generated using Quiz" +
                        f" Master 2022 on {todays_date}.\n\n" +
                        f"https://quiz-master-2022.herokuapp.com/"
                    },
                    "updateMask": "*"
                }
            },
            form_questions
        ]
    }

    return body


def add_item_to_gform(item, form_id):
    """
    Adds a Question to Google Form

    Args:
    item: Item to add to the Google Form
    form_id: The ID of the form to add the item to
    """
    body_text = {
        "requests": [
            item
        ]
    }
    try:
        FORM_SERVICE.forms().batchUpdate(
            formId=form_id, body=body_text).execute()
    except errors.HttpError as error:
        cprint(f"🚫 An error occurred: {error}", "red")


def create_google_form(game_obj):
    """
    Create a new Google Form using a Quiz Game Object

    Args:
    game_obj: A Quiz Game Object
    """

    # Boilerplate code for initial form setup
    BOILER_PLATE = {
        "info": {
            "title": game_obj.get_quiz_title(),
            "documentTitle": game_obj.get_quiz_title()
        }
    }

    # Creates the initial form
    QUIZ_FORM = FORM_SERVICE.forms().create(body=BOILER_PLATE).execute()
    QUIZ_FORM_ID = QUIZ_FORM["formId"]
    QUIZ_FORM_URL = QUIZ_FORM["responderUri"]

    update = create_gform_body(game_obj)

    question_setting = FORM_SERVICE.forms().batchUpdate(
        formId=QUIZ_FORM_ID, body=update).execute()

    team_name_q = create_gform_text_question("Team Name")

    add_item_to_gform(team_name_q, QUIZ_FORM_ID)

    # Print the result to see it's now a quiz
    getresult = FORM_SERVICE.forms().get(formId=QUIZ_FORM["formId"]).execute()

    clear()
    cprint(f"Your Google Form Quiz is ready to share: \n", "green")
    # print(f"Form ID: {QUIZ_FORM_ID}")
    print(f"{QUIZ_FORM_URL} \n")

    # Ask would the user like to see responses to the form
    print("You can now share this quiz form with friends!")
    ask_form_owner = False
    ask_form_owner = ask_yes_no(
        "Would you like to be an owner of this form to see their responses?")

    while ask_form_owner:
        email = input("\nPlease enter the e-mail address of your Google "
                      "Account or enter Q to quit:\n\n")
        email = email.lower()

        # Quit to main menu if user types Q or quit
        if is_quit(email):
            break

        # Try validate the email address, if valid share Google Form
        try:
            email = validate_email(email).email

            ask_form_owner = False
            insert_permission(DRIVE_SERVICE, QUIZ_FORM_ID, email, "writer")
            cprint("\n\n📨 An e-mail is on the way! Happy Quizzing!\n\n",
                   "green")

            ask_any_key()

            break

        except EmailNotValidError as e:
            print(str(e))
            continue

        else:
            cprint("📧 Please enter a valid e-mail address!", "red")
            continue
