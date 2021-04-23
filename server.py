
# FLASK DOCUMENTATION: https://flask.palletsprojects.com/en/1.1.x/quickstart/
# FLASK variables: https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
# ANIMATIONS: https://giphy.com/

# 1. CREATING APPLICATION:

import random
from flask import Flask
app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


# HOME ROUTE:
@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<h2>Enter your number into URL: </h2>' \
           '<h3>example (http://127.0.0.1:5000/your number) </h3>' \
           '<img src="https://media.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif">'

# NUMBER ROUTE:
@app.route('/<int:number>')
def number_choice(number):
    if number < random_number:
        return f'<h1>{number} is too low, try again! </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    elif number > random_number:
        return f'<h1> {number} is too high, try again! </h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    else:
        return f'<h1>and {number} is just right! </h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
