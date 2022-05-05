from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from apiclient import discovery
import json
from email_validator import validate_email, EmailNotValidError
from helpers import ask_yes_no, is_quit
from termcolor import colored, cprint
from gdrive_utility import insert_permission, DRIVE_SERVICE
from create_gform_items import (
    create_gform_question, create_gform_round,
    create_gform_text_question, create_gform_game)

# https://google-auth.readthedocs.io/en/master/user-guide.html

CREDS = service_account.Credentials.from_service_account_file("creds.json")

SCOPED_CREDENTIALS = CREDS.with_scopes(
    ["https://www.googleapis.com/auth/forms.body"])

DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

FORM_SERVICE = discovery.build("forms", "v1", credentials=SCOPED_CREDENTIALS,
                               discoveryServiceUrl=DISCOVERY_DOC,
                               static_discovery=False)

# End of Authorisation Code

# Boilerplate code for initial form setup
form = {
    "info": {
        "title": "My New Quiz"
    }
}

# Creates the initial form
QUIZ_FORM = FORM_SERVICE.forms().create(body=form).execute()
QUIZ_FORM_ID = QUIZ_FORM["formId"]
QUIZ_FORM_URL = QUIZ_FORM["responderUri"]


# Convert the form into a quiz & create and add all the questions
def create_gform_body(game_obj):
    """
    Returns the request body to send to the Google Forms
    API for a new Quiz Game

    Args:
    game_obj: A Quiz Game Object
    """

    form_questions = create_gform_game(game_obj)

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
                        "description": f""
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
    FORM_SERVICE.forms().batchUpdate(
        formId=form_id, body=body_text).execute()


# Updates the form

def create_google_form(game_obj):
    """
    Create a new Google Form using a Quiz Game Object

    Args:
    game_obj: A Quiz Game Object
    """

    update = create_gform_body(game_obj)

    question_setting = FORM_SERVICE.forms().batchUpdate(
        formId=QUIZ_FORM_ID, body=update).execute()

    team_name_q = create_gform_text_question("Team Name")

    add_item_to_gform(team_name_q, QUIZ_FORM_ID)

    # Print the result to see it's now a quiz
    getresult = FORM_SERVICE.forms().get(formId=QUIZ_FORM["formId"]).execute()

    print(f"Form ID: {QUIZ_FORM_ID}")
    cprint(f"Your Google Form Quiz is ready to share: \n", "green")
    print(f"{QUIZ_FORM_URL} \n")

    # Ask would the user like to see responses to the form
    print("You can share this form with friends and see their responses")
    ask_form_owner = False
    ask_form_owner = ask_yes_no(
        "Would you like to be added as an owner of this form?")

    while ask_form_owner:
        input("Please enter the e-mail address of your Google Account "
              "or enter Q to quit.\n\n")
        email = input("E-mail Address: \n").lower()

        # Quit to main menu if user types Q or quit
        if is_quit(email):
            break

        # Try validate the email address, if valid share Google Form
        try:
            email = validate_email(email).email

            ask_form_owner = False
            insert_permission(DRIVE_SERVICE, QUIZ_FORM_ID, email, "writer")
            cprint("📨 An e-mail is on the way! Happy Quizzing!")

            break

        except EmailNotValidError as e:
            print(str(e))
            continue

        else:
            print("📧 Please enter a valid e-mail address!")
            continue
