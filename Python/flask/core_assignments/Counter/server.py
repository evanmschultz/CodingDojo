from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
# Set secret key to access session, update using environment variable if deploying
app.secret_key = 'secret_key'


@app.route('/')
def index():
    '''Root route, increments real and user input visits when route is called'''

    # The amount of visits based on user inputs
    session['visits'] = session.get('visits', 0) + 1
    print(f'\n{"_"*50}\n\nPage visits: {session["visits"]}\n{"_"*50}\n')

    # Real amount of times the client visited the page
    session['real_visits'] = session.get('real_visits', 0) + 1
    print(
        f'\n{"_"*50}\n\nPage real_visits: {session["real_visits"]}\n{"_"*50}\n')

    return render_template('index.jinja2', visits=session['visits'], real_visits=session['real_visits'])


@app.route('/increment', methods=['POST'])
def increment():
    '''Increments visits by 1 or 2 on button push'''

    # Get amount from requests dictionary, args: 'amount', default=1
    amount = int(request.args.get('amount', 1))

    # Update session dictionary 'visits', subtract 1 because of logic on root route
    session['visits'] = session.get('visits', 0) + amount - 1
    print(f'\n{"_"*50}\n\nPage visits:{session["visits"]}\n{"_"*50}\n')

    return redirect('/')


@app.route('/increment_by', methods=['POST'])
def increment_by():
    '''Increments visits by amount specified by user input'''

    # Get inputted amount from form
    increment_by = request.form['increment_by']
    print(f'\n{"_"*50}\n\n{increment_by}\n{"_"*50}\n')

    # Update session dictionary 'visits', subtract 1 because of logic on root route
    session['visits'] = session.get('visits', 0) + int(increment_by) - 1
    print(f'\n{"_"*50}\n\nPage visits:{session["visits"]}\n{"_"*50}\n')

    return redirect('/')  # Route to root


@app.route('/reset', methods=['POST'])
def reset():
    '''Clears visits from session dictionary'''

    print(f'\n{"_"*50}\n\nPage visits reset\n{"_"*50}\n')

    session.pop('visits')
    session.pop('real_visits')

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
