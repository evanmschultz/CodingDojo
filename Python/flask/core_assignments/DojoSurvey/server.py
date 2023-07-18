from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

# Set secret key to access session, update using environment variable if deploying
app.secret_key = 'secret_key'


@app.route('/')
def index():
    '''Root route, display form inputs'''

    return render_template('index.jinja2')


@app.route('/submit', methods=['POST'])
def submit_form():
    '''Route handles logic to save form submission to session'''

    session['name'] = request.form.get('name', '').title()
    print('Name: ', session['name'])

    session['dojo_location'] = request.form.get('dojo_locations', '').title()
    print('Dojo location: ', session['dojo_location'])

    session['favorite_language'] = request.form.get(
        'favorite_language', '').title()
    print('Favorite language: ', session['favorite_language'])

    session['comments'] = request.form.get('comments', '')
    print('Comments: ', session['comments'])

    return redirect('/results')


@app.route('/results')
def results():
    '''Displays results from form submission'''
    name = session['name']
    dojo_location = session['dojo_location']
    favorite_language = session['favorite_language']
    comments = session['comments']

    return render_template('results.jinja2', name=name, dojo_location=dojo_location, favorite_language=favorite_language, comments=comments)


@app.route('/reset', methods=['POST'])
def reset():
    '''Clears session and returns to root'''

    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
