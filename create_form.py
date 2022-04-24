from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from apiclient import discovery
import json
from create_question import dummy_round, create_gform_question, create_gform_round

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
result = form_service.forms().create(body=form).execute()


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
                        "description": f"Round No. {round_num}: {round_category}"
                    },
                    "updateMask": "description"
                }
            },
            create_gform_round(round_obj)
        ]
    }


    return body


update = create_google_form("My First Quiz", dummy_round)

# print(update)

# Updates the form
question_setting = form_service.forms().batchUpdate(formId=result["formId"],
                                                    body=update).execute()

# Print the result to see it's now a quiz
getresult = form_service.forms().get(formId=result["formId"]).execute()

print(getresult)

form_id = getresult["formId"]
print(f"Form ID = {form_id}")
