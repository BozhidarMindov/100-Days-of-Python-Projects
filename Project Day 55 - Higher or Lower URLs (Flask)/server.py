from flask import Flask
import random


app = Flask(__name__)


@app.route('/')
def home_screen():
    return "<h1>Guess a number between 0 and 9</h1>" \
           '<iframe src="https://giphy.com/embed/IdlrlhB1Rts6fQRjdb" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


@app.route('/<int:number>')
def guess(number):
    random_num = random.randint(0, 9)
    if number < 1 or number > 10:
        return"<h1 style='black: red'>The number you guessed is outside of range!</h1>" \
               '<iframe src="https://giphy.com/embed/y4E6VumnBbIfm" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
    elif number < random_num:
        return "<h1 style='color: green'>Too low!</h1>" \
                '<iframe src="https://giphy.com/embed/l1BgRBd4cVC8OaZKo" width="480" height="296" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
    elif number > random_num:
        return "<h1 style='color: red'>Too high!</h1>" \
               '<iframe src="https://giphy.com/embed/2cei8MJiL2OWga5XoC" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
    elif number == random_num:
        return "<h1 style='color: purple'>You got it!</h1>" \
               '<iframe src="https://giphy.com/embed/3oriNW5rslDXcDvu1i" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


if __name__ == "__main__":
    app.run()