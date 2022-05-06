
# Quiz Master 2022

[![](documentation/images/screenshot-welcome.png)](https://quiz-master-2022.herokuapp.com/)

[Link to Live Site](https://quiz-master-2022.herokuapp.com/)


## Introduction

The project is a Python command line application which can create and play quiz games using an consisting of several rounds based on the user's desired configuration.

The user can play along in the terminal, or export a quiz to Google Forms where they can share it with friends where they will be automatically graded.

I was frustrated by the difficulties faced writing and grading a virtual table quiz and was inspired to make an application to automate the process.


## User Stories

- As a first time user, I need instructions on how to use the applications so I can use it.

- As a user, I want to be able to play a quick quiz round without chosing any settings.

- As a quiz enthusiast I want to be able to build custom quizzes based on different categories.

- As a user running a virtual quiz, I want to be able to create a custom quiz to share and play with my friends.


## 



## UX  

I used Lucid Chart to plan the flow of the application before coding.

![Flow Chart of the Application](documentation/images/flow-chart-menu.png)


To make the application easy to navigate, numbers are used for most responses unless the user needs to type a name for their Quiz.

The user can quit to the main menu at any stage, and validation is used on all input to check inputs and ensure the application doesn't crash.

The terminal screen is regularly cleared to ensure the terminal doesn't get cluttered and confuse the user between input prompts.

Coloured text was used sparingly for correct/incorrect answer messages and warnings.


### Typography

I chose Courier New (or other monospace font as fallback) to match the text of the Python Terminal, and as it is one of the most commonly available web-safe fonts.


### Wireframes

![](documentation/images/wireframe-deploy.png)


## Features 


### Existing Features

***

#### Main Menu

```
Main Menu
_________

Please choose from the following:

(1) Play Quick Quiz Round
(2) Create Custom Quiz
(3) Create a Google Form Quiz
(4) Help

Press Enter to confirm your selection. 
```

The user is presented with four options and can select where to navigate to by entering the coresponding number.

Validation is used to ensure they only enter a valid option.

At any point after this menu, the user can enter `Quit` or `Q` to return back to the Main Menu.


#### Play Quick Quiz Round

The application creates a short quiz of 5 General Knowledge questions for the user to play immediately.


#### Create Custom Quiz

The user can select custom options for a quiz, and play through the quiz.


#### Create Google Form Quiz

The user can create a custom quiz, and they will recieve a Google Form link where they can play the Quiz and send it to friends for the purposes of running a virtual table quiz.

Optionally, they can add their Google Account e-mail address to be added as a owner of the form, so they can see all the responses/results and edit the form if desired.


#### Help

This screen provides further information on using the application, with a detailed description of the different menu options.


__Game Area__

I wanted to write `create_quiz.py` to make it as reusable as possible, so it could easily be used in other Quiz projects. I took the data returned from the Open Trivia Database, and created Python objects using classes.

A Game Object contains 1 or more Round objects, which in turn contain 1 or more Question objects. 


```python
class Game:
    def __init__(self, quiz_title, num_rounds, num_qs, categories, difficulty):
        self.quiz_title = quiz_title
        self.num_rounds = num_rounds
        self.num_questions = num_qs
        self.categories = categories
        self.difficulty = difficulty

        self.rounds = [Round(x+1, self.num_questions, self.categories[x],
                             self.difficulty) for x in range(self.num_rounds)]

```

```python
class Round:

    def __init__(self, round_num, num_qs, category, difficulty):

        self.round_num = round_num
        self.num_qs = num_qs
        self.category = category
        self.difficulty = difficulty

        self.question_data = get_quiz_questions(num_qs, category, difficulty)

        self.questions_list = [Question(**question)
                               for question in self.question_data]
```

```python
class Question:

    def __init__(
        self, category, type, difficulty, question,
            correct_answer, incorrect_answers):

        self.category = category
        self.qtype = type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
```

***

#### Google Drive Utility Menu

- When building the project, I needed a way to use the Google Drive API to manage the forms created. I build a simple file management tool, and implemented it as a secret menu option from the Main Menu.

- To access the Google Drive Utility, you enter 999 on the Main Menu and are then prompted for a password.

- I implemented the administrator password similar to the API keys, storing it in a variable in `creds.json` file which wasn't pushed to Heroku. In the Heroku project settings I stored it as a Config Var, ensuring it is never publically exposed.

- As the Utility is only available to an administrator, I have included screenshots below.


![Screenshot showing the password prompt for the Google Drive Utility](documentation/images/screenshot-gdrive-1.png)
![Screenshot showing the menu for the Google Drive Utility with 3 options - List All Files, Delete File by ID, Delete all Files](documentation/images/screenshot-gdrive-2.png)
![Screenshot showing the the Google Drive Utility listing all the created Forms and their IDs](documentation/images/screenshot-gdrive-3.png)

***


### Features Left to Implement

- The project could be built out to include 


## Technologies Used

- [Python](https://www.python.org/)
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for storing the repository online during development.
- GitHub Projects was invaluable throughout the project and helped me keep track of things to do and bugs to fix - you can see [the project's board here](https://github.com/users/davidindub/projects/3).
- [GitPod](https://gitpod.io/) as a cloud based IDE.
- [Google Forms API](https://developers.google.com/forms) and [Google Drive API](https://developers.google.com/drive) for creating and sharing the generated Google Forms.
- [favicon.io](https://favicon.io/favicon-generator/) to make a favicon for site.
- [Google Chrome](https://www.google.com/intl/en_ie/chrome/), [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Safari](https://www.apple.com/safari/) for testing on macOS Monterey, Windows 10, iOS 15, iPadOS 15 and Android 10.
- [Concepts](https://concepts.app/en/) for sketching on an iPad.
- [Lucid Chart](https://lucid.app/) for making flow charts.

## Python Packages Used

- [termcolor](https://pypi.org/project/termcolor/) for colored terminal text.
- [art](https://github.com/sepandhaghighi/art) - ASCII art library for ASCII text.
- [google-auth](https://pypi.org/project/google-auth/) & [google.oauth2](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.html) for authenticating with Google APIs.
- [email-validator](https://pypi.org/project/email-validator/) for validating the user's e-mail address if they want the Google Form Quiz shared with their Google Account.


## Testing 

I performed manual testing contiously as the application was being developed.

I used the `pprint` package at some stages of development to more easily see objects I was printing to the terminal.

I used test JSON quiz data stored in a variable to test the Google Forms creation functions as I was building them.

The [GitHub Issues](https://github.com/davidindub/quiz-master/issues) page of the repository was invaluble for tracking bugs found, and closing the issues when fixed.

I deployed on Heroku early so I could see the final input as it differs to the terminal in my development environment.
I had to limit the amount of text displayed at any time to prevent a scroll appearing, such as on the help screen and listing the available categories.


### Challenges Faced

- The [Google Forms API](https://developers.google.com/forms) was only released in March 2022, the month before I started building the project. Unlike other products like Google Sheets, there was are no Python Packages released yet to simplify using the Forms API.
- I had to build the project using just the documentation and there was a lack of any examples of the Forms API in use in a Python project yet.
- I think there's great potential for a Google Forms API Package, and it's a project I would like to work on in future.
- I faced difficulties with the encoding of the data from the API and escape characters appearing when I passed the data to Google Forms. I used `urllib.parse.urlparse` to parse the Quiz API data. Using square bracket notation to access the properties of the Quiz/Round/Game objects for the Google Form creation was introducing encoding errors, so I created methods on the objects that return the properies.



### Validation

I used `# noqa` on line 44 of `create_quiz.py` ignore a line length warning on a long URL for an API call.

http://pep8online.com/


***



## Deployment

Due to a recent [security breach](https://status.heroku.com/incidents/2413) of Heroku OAuth Tokens, GitHub actions deployment to Heroku was disabled.

The required Procfile for Heroku was included in the Code Institute Python Essentials Template (see [Content](#credits) section)

I instead deployed to Heroku using the Heroku CLI with the following steps
    - Create a new App in the Heroku web dashboard named 'quiz-master-2022'
    - In the Heroku Dashboard Settings, under Config Vars - add the contents of the `creds.json` file which wasn't pushed to a variable called `CREDS`
    - Under Buildpacks, add Python and Nodejs and click save.
    - run `heroku login -i` in the command line directory of the project
    - Enter my Heroku account login details
    - run `heroku git:remote -a quiz-master-2022` to set git remote heroku to https://git.heroku.com/quiz-master-2022.git
    - run `git push heroku main` to push to Heroku


In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/davidindub/quiz-master.git`


Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/davidindub/quiz-master)

***

After cloning or opening the repository in Gitpod, you will need to:

1. Create your own `creds.json` with the Google API details in this format:

```json
{
    "type": "",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "",
    "client_x509_cert_url": ""
  }
```

2. Run `pip3 install -r requirements.txt` to install required Python packages.

## Credits 

### Content 

- I began with the [Code Institute Python Essentials](https://github.com/Code-Institute-Org/python-essentials-template) template and customised the the HTML & CSS. The template allows the Python application to run in the browser using a terminal build with [Node.js](https://nodejs.org/en/).
- [Open Trivia Database](https://opentdb.com/) for the quiz questions.
- The code for the custom greeting based on the time of day I originally wrote for another application, [Coffee Calculator](https://github.com/davidindub/coffee-calculator/blob/main/greeting.py)
- [Google Forms API](https://developers.google.com/forms) and [Google Drive API](https://developers.google.com/drive) documentation for their quickstart guides on using the APIs.
- [Stack Overflow: Clear terminal in Python](https://stackoverflow.com/questions/2084508/clear-terminal-in-python) for the code to clear the terminal screen.


### Media


### Acknowledgements

- Thank you to my CI Mentor [Tim Nelson](https://github.com/TravelTimN) for his help and suggestions.
- Thanks to my partner David for his constant support on my journey to a new career.