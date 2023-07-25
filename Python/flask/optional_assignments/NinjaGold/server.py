from datetime import datetime
from flask import Flask, Response, abort, render_template, request, redirect, session
from werkzeug.wrappers.response import Response
from random import randint, choices


# Instantiate a Flask instance
app = Flask(import_name=__name__)

# Set a secret key for security purposes
app.secret_key = 'secret_key'


@app.route(rule='/')
def home() -> str:
    """
    Home Route

    This route is the homepage of the web application. And displays a form for the user to 
    pick actions that get them Ninja Gold. The user can pick from Farm, Cave, House, or Casino.
    Actions are displayed in a table below the form.

    :methods: GET
    :url: /

    :return: Rendered homepage template.
    """

    # Check if session['gold'] exists, if not create it and set it to 0
    if 'gold' not in session:
        session['gold'] = 0

    # Check if session['activities'] exists, if not create it and set it to an empty list
    if 'activities' not in session:
        session['activities'] = []

    # print(
    #     f'\n{"_"*70}\n\nGold = {session["gold"]} | Activities = {session["activities"]}\n{"_"*70}\n')

    # Render the homepage template
    return render_template(template_name_or_list='index.jinja2')


@app.route(rule='/process_money', methods=['POST'])
def process_money() -> Response:
    """
    Process Money Route

    This route processes the user's form submission and updates the session['gold'] and
    session['activities'] variables.

    :methods: POST
    :url: /process_money

    :return: Redirect to the homepage.
    """

    # Check if the user submitted the form
    if request.method == 'POST':
        amount: int = 0
        building: str = ''

        # Dictionary of gold ranges for each building
        gold_ranges: dict = {
            'farm': (10, 20),
            'cave': (5, 10),
            'house': (2, 5),
            # The casino losses are calculated below in the conditional
            'casino': (0, 50)
        }

        # Set building variable to the user's form submission
        building = request.form['building']

        # Set amount variable to a random integer within the gold range for the building
        amount = randint(a=gold_ranges[building]
                         [0], b=gold_ranges[building][1])

        # Check if the building is the casino
        if building == 'casino':

            """
                Update amount by multiplying by 1 (40% chance) or -1 (60% chance) as the casino 
                gives the user a 55% chance of losing and 45% chance of winning gold respectively.
            """
            amount *= choices(population=[-1, 1], weights=[0.60, 0.40], k=1)[0]

        # Update session['gold']
        session['gold'] += amount

        # Update session['activities'] with conditional for if user earned or lost gold
        if amount > 0:
            session['activities'].append(
                f'Earned {amount} gold from the {building}! On {datetime.now().strftime("%m/%d/%Y at %H:%M:%S")}')
        elif amount < 0:
            session['activities'].append(
                f'Entered a {building} and lost {amount} gold... Ouch... On {datetime.now().strftime(f"%m/%d/%Y at %H:%M:%S")}')
        else:
            session['activities'].append(
                f'Entered a {building} and broke even! On {datetime.now().strftime(f"%m/%d/%Y at %H:%M:%S")}')

        # Redirect to the homepage
        return redirect(location='/')

    # If the request method is not POST, return an error.
    abort(405)  # HTTP 405 - Indicates - Method Not Allowed


@app.route(rule='/reset', methods=['POST'])
def reset() -> Response:
    """
    Reset Route

    This route resets the session['gold'] and session['activities'] variables.

    :methods: POST
    :url: /reset

    :return: Redirect to the homepage.
    """

    # Check if the user submitted the form
    if request.method == 'POST':

        # Reset session['gold'] and session['activities']
        session['gold'] = 0
        session['activities'] = []

        # Redirect to the homepage
        return redirect(location='/')

    # If the request method is not POST, return an error.
    abort(405)  # HTTP 405 - Indicates - Method Not Allowed


if __name__ == "__main__":
    app.run(debug=True)
