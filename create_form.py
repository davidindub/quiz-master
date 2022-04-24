from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from apiclient import discovery
import json
from create_gform_items import TEST_ROUND, create_gform_question, create_gform_round, create_gform_text_question

# https://google-auth.readthedocs.io/en/master/user-guide.html

credentials = service_account.Credentials.from_service_account_file(
    'client_secrets.json')

scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/forms.body'])

DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

form_service = discovery.build('forms', 'v1', credentials=scoped_credentials,
                               discoveryServiceUrl=DISCOVERY_DOC,
                               static_discovery=False)

# End of Authorisation Code

form = {
    "info": {
        "title": "My new quiz",
    }
}

# Creates the initial form
QUIZ_FORM = form_service.forms().create(body=form).execute()
QUIZ_FORM_ID = QUIZ_FORM["formId"]
QUIZ_FORM_URL = QUIZ_FORM["responderUri"]


# JSON to convert the form into a quiz & add description to a Form
def create_google_form(quiz_name, round_obj):
    """
    Returns the request body to send to the Google Forms
    API for a new Quiz Round

    Args:
    quiz_name: Name for the Quiz
    round_obj: Object containing a quiz round
    """
    round_num = round_obj["round_num"]
    round_category = round_obj["question_data"][0]["category"]

    form_questions = create_gform_round(round_obj)

    # create_gform_text_question("Team Name")

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
                        "title": quiz_name,
                        "description": f"Round {round_num}: {round_category}"
                    },
                    "updateMask": "*"
                }
            },
            form_questions
        ]
    }

    return body


update = create_google_form("My First Quiz", TEST_ROUND)

# Updates the form
question_setting = form_service.forms().batchUpdate(formId=QUIZ_FORM_ID,
                                                    body=update).execute()


def add_item_to_gform(item):
    """
    Adds a Question to Google Form
    """
    body_text = {
        "requests": [
            item
        ]
    }
    form_service.forms().batchUpdate(formId=QUIZ_FORM_ID, body=body_text).execute()


team_name_q = create_gform_text_question("Team Name")

add_item_to_gform(team_name_q)

# Print the result to see it's now a quiz
getresult = form_service.forms().get(formId=QUIZ_FORM["formId"]).execute()

# print(getresult)

print(f"Form ID: {QUIZ_FORM_ID}")
print(f"Form URL: {QUIZ_FORM_URL}")
