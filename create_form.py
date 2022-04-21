from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from apiclient import discovery
# from httplib2 import Http

# https://google-auth.readthedocs.io/en/master/user-guide.html

credentials = service_account.Credentials.from_service_account_file(
    'client_secrets.json')

scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/forms.body'])

DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

form_service = discovery.build('forms', 'v1', credentials=scoped_credentials, discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# End of Authorisation Code

form = {
    "info": {
        "title": "My new quiz",
    }
}

# Creates the initial form
result = form_service.forms().create(body=form).execute()

# JSON to convert the form into a quiz
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
        }
    ]
}

# Converts the form into a quiz
question_setting = form_service.forms().batchUpdate(formId=result["formId"],
                                                    body=update).execute()

# Print the result to see it's now a quiz
getresult = form_service.forms().get(formId=result["formId"]).execute()
print(getresult)