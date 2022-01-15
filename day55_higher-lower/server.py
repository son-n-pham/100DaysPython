from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Guess a number between 0 and 9<h1><br>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<user_number>")
def user_input(user_number):
    user_number = int(user_number)
    if user_number < random_number:
        return "<h2 style='color:red'>Too low, try again!<h2>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif user_number > random_number:
        return "<h2 style='color:purple'>Too high, try again!<h2>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h2 style='color:purple'>You found me!<h2>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    # If running app.run(), debug mode is off as default. To turn the debug mode on, just do the syntax app.run(debug=True)
    random_number = random.randint(0, 10)
    app.run(debug=True)
