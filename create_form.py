from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from apiclient import discovery
import json
# from httplib2 import Http
from create_question import dummy_question, create_gform_question

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

# Makes a sample question to insert to form
question_to_insert_to_form = create_gform_question(dummy_question)

# JSON to convert the form into a quiz & add description to a Form
update = {
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
                    "description": "Please complete this quiz based on this week's readings for class."
                },
                "updateMask": "description"
            }
        },
        question_to_insert_to_form
    ]
}

# Updates the form
question_setting = form_service.forms().batchUpdate(formId=result["formId"],
                                                    body=update).execute()

# Print the result to see it's now a quiz
getresult = form_service.forms().get(formId=result["formId"]).execute()

print(getresult)

form_id = getresult["formId"]
print(f"Form ID = {form_id}")
