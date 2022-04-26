
# QuizMaster


[Link to Live Site](https://www.)


## Introduction

The project is a Python command line application which can create quiz games using an consisting of several rounds based on the user's desired configuration.

The user can play along in the terminal, or export a quiz to Google Forms where they can share it with friends where they will be automatically graded.


## User Stories

As a first time user, I need instructions on how to use the applications so I can use it.

As a user, I want to be able to play a quick quiz round without leaving the terminal.

As a quiz enthusiast I want to be able to build custom quizzes based on different categories.

As a user, I want to be able to create a custom quiz to share and play with my friends.


## UX  


### Colour Scheme
 

### Typography


### Wireframes


## Features 

### Existing Features

***

__Game Area__

***

__Accessibility__

***

__Favicon__


***

### Features Left to Implement


## Technologies Used

- [Python](https://www.python.org/)
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for storing the repository online during development.
- GitHub Projects was invaluable throughout the project and helped me keep track of things to do and bugs to fix - you can see [the project's board here](https://github.com/users/davidindub/projects/2).
- [GitPod](https://gitpod.io/) as a cloud based IDE.
- [Google Forms API](https://developers.google.com/forms) and [Google Drive API](https://developers.google.com/drive) for creating and sharing the generated Google Forms.
- [favicon.io](https://favicon.io/favicon-generator/) to make a favicon for site.
- [Google Chrome](https://www.google.com/intl/en_ie/chrome/), [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Safari](https://www.apple.com/safari/) for testing on macOS Monterey, Windows 10, iOS 15, iPadOS 15 and Android 10.
- [Concepts](https://concepts.app/en/) for sketching on an iPad.
- [Lucid Chart](https://lucid.app/) for making flow charts.

## Testing 


## Deployment

Due to a recent [security breach](https://status.heroku.com/incidents/2413) of Heroku OAuth Tokens, GitHub actions deployment to Heroku was disabled.

I instead deployed to Heroku using the Heroku CLI with the following steps
    - Create a new App in the Heroku web dashboard named 'quiz-master-2022'
    - In the Heroku Dashboard Settings, under Config Vars - add the contents of the `client_secrets.json` file which wasn't pushed to a variable called `credentials`
    - Under Buildpacks, add Python and Nodejs and click save.
    - run `heroku login -i` in the command line directory of the project
    - Enter my Heroku account login details
    - run `heroku git:remote -a quiz-master-2022` to set git remote heroku to https://git.heroku.com/quiz-master-2022.git
    - run `git push heroku main` to push to Heroku


In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/davidindub/quiz-master.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/davidindub/quiz-master)


## Credits 

### Content 

- [Open Trivia Database](https://opentdb.com/) for the quiz questions.
- The code for the custom greeting based on the time of day I originally wrote for another application, [Coffee Calculator](https://github.com/davidindub/coffee-calculator/blob/main/greeting.py)
- [art - ASCII art library for Python](https://github.com/sepandhaghighi/art) for ASCII art.
- [Google Forms API](https://developers.google.com/forms) and [Google Drive API](https://developers.google.com/drive) documentation for their quickstart guides on using the APIs.


### Media


### Acknowledgements

- Thank you to my CI Mentor [Tim Nelson](https://github.com/TravelTimN) for his help and suggestions.
- Thanks to my partner David for his constant support on my journey to a new career.