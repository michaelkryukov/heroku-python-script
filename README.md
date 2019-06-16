# Template for hosting python scripts and applications on Heroku

This is a small example of running your script with
[Heroku](https://www.heroku.com/). You can run almost any python application
with any dependencies.

## Getting Started

1. Download or clone this repository
2. Register on [Heroku](https://www.heroku.com/)
3. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
4. Download and install [git](https://git-scm.com/downloads)
5. Copy your script or project to this repository's folder
6. Replace "script.py" with the path to your main executable file in `Procfile`

   ```procfile
   worker: python script.py
   ```

   > If you are getting errors, you can try replace `worker` with `web`.
7. You may select your python version and runtime using `runtime.txt`. Read
   how on [official heroku page](https://devcenter.heroku.com/articles/python-runtimes#selecting-a-runtime).
8. If you are using any not built-in modules, you must add them to your
   `requirements.txt`. To check which version of the module you have, run
   `pip freeze` in the terminal. You will get lines with information about
   installed modules and their versions in the format like
   `MODULE_NAME==MODULE_VERSION`. Add lines with required modules and their
   versions to your `requirements.txt`. Don't keep unused modules in
   `requirements.txt`. This file should contain every module your application
   needs. Heroku will install modules from this file automatically.
9. Open terminal (or do it another way, but I will explain how to do it in
   the terminal on Ubuntu) and create a git repository.
   1. Initiate git repository

      ```bash
      git init
      ```

   2. Create heroku application

      ```bash
      heroku create
      ```

   3. Add, commit and push your code into branch `master` of the
      remote `heroku`.

      ```bash
      git add .
      git commit -m "initial commit"
      git push heroku master
      ```

10. Specify the amount of worker that will run your application

    ```bash
    heroku ps:scale worker=1
    ```

11. Now everything should be working. You can check your logs with this command

    ```bash
    heroku logs --tail
    ```

12. You can open the URL where the script is deployed using the below
    command (if you are deploying web application)

    ```bash
    heroku open
    ```

13. From now on you can use usual git commands (push, add, commit, etc.)
    to update your app. Every time you `push heroku master` your
    app gets redeployed with updated source code

14. To stop your application scale down the amount of workers with like this

     ```bash
    heroku ps:scale worker=0
    ```

### Prerequisites

* [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
* [git](https://git-scm.com/downloads)

## Authors

* @michaelkrukov - https://michaelkrukov.ru/

## Acknowledgments

* [Official guide to deploy app](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [Official guide about worker](https://devcenter.heroku.com/articles/background-jobs-queueing)
* [Guided "Simple twitter-bot with Python, Tweepy and Heroku"](http://briancaffey.github.io/2016/04/05/twitter-bot-tutorial.html)
