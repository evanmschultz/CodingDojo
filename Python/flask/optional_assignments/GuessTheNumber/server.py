from flask import Flask, render_template, redirect, session, request
from random import randint

app = Flask(__name__)
# Set secret key to access session, update using environment variable if deploying
app.secret_key = 'secret_key'


@app.route('/')
def index():
    '''Root route'''

    # Check if a random number has been generated
    if 'number' not in session:
        session['number'] = randint(1, 100)
    print(f'\n{"_"*50}\n\nRandom Number: {session["number"]}\n{"_"*50}\n')

    # Retrieve message from session, default to empty string if not present
    message = session.pop('message', '')

    return render_template('index.jinja2', message=message)


@app.route('/guess', methods=['POST'])
def guess():
    '''Checks user's guess and sets the appropriate message in the session'''

    try:
        # Check if input is a valid number, if so, set guess variable to input
        guess = int(request.form.get('guessed_number', 0))
    except:
        # Inform user to input a valid number, redirect to root
        session['message'] = 'Input a valid integer'
        return redirect('/')

    # Check for guess count, if not in session add it, else increment it
    if 'guess_count' not in session:
        session['guess_count'] = 1
    else:
        session['guess_count'] += 1

    if session['guess_count'] >= 5:
        session['message'] = f'<p>You Lost!<br>I was thinking of {session["number"]}.</p>'

        # Clear session
        session.pop('number')
        session.pop('guess_count')

        return redirect('/')

    if guess < session['number']:
        session['message'] = '<p>Too Low!</p>'
    elif guess > session['number']:
        session['message'] = '<p>Too High!</p>'
    else:
        if session['guess_count'] == 1:
            try_string = 'try'
        else:
            try_string = 'tries'
        # Render success
        session['message'] = f'<p>Correct! I was thinking of was {guess}.<br>It only took you {session["guess_count"]} {try_string} to get it!</p>'

        # Clear number, and guess_count
        session.pop('number')
        session.pop('guess_count')

    # Redirect to root with message
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    '''Resets "Thinking of" number'''

    if 'number' in session:
        session.pop('number')

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
