# Template for Python Script hosted on Heroku

This is small example of running your own bots with [Heroku](https://www.heroku.com/).
You can run ANY python script with ANY dependaries.

## Getting Started

1. Download this repository. 
2. Register on [Heroku](https://www.heroku.com/).
3. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
4. Download and install [git](https://git-scm.com/downloads).
5. Copy your script/ project to repository's folder.
6. Replace "script.py" with path to your main executable file in "Procfile".
   ```
   worker: python script.py
   ```
   
8. You may select your python version and runtime with "runtime.txt". Read how on [official heroku page](https://devcenter.heroku.com/articles/python-runtimes#selecting-a-runtime).
9. If you are using non-standart modules, you must add them to requirements.txt
   
   To check which version of module you have on your computer, run pip freeze | grep MODULE_NAME in the terminal. 
   
   You will get line MODULE_NAME==MODULE_VERSION. Add this line to "requirements.txt".
   
   You should remove any unused modules from "requirements.txt".
   
   Repeat this process for all the modules you are planning to use.
   
10. Now open terminal(or do it other way, but i will explain how to do it in terminal on Ubuntu) and create git repository.
   
   ```
   git init
   ```
   
   Create heroku app.
   
   ```
   heroku create
   ```
   
   And push your code into heroku app.
   
   ```
   git add .
   git commit -m "initial commit"
   git push heroku master
   ```

11. Run you worker with following command.
   ```
   heroku ps:scale worker=1
   ```
   
12. Now everything should be working. You can check your logs with.

   ```
   heroku logs --tail
   ```
   
13. From now on you can use usual git commands(push, add, commit etc.) to update your app.

   Everytime you push heroku master your app gets redeployed.

### Prerequisites

* [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
* [git](https://git-scm.com/downloads)

## Authors

* @michaelkrukov - http://michaelkrukov.ru/

## License

This project is licensed under GNU General Public License v3.0 - see the [LICENCE.md](LICENCE.md) file for details

## Acknowledgments

* [Official guide to deploy app](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [Official guide about worker](https://devcenter.heroku.com/articles/background-jobs-queueing)
* [Guided "Simple twitter-bot with Python, Tweepy and Heroku"](http://briancaffey.github.io/2016/04/05/twitter-bot-tutorial.html)
