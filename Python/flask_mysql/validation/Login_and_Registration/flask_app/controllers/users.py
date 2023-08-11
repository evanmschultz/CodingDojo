from typing import Dict, Optional
from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session, flash, url_for

# Type hinting imports
from werkzeug import Response


@app.route('/', methods=['GET'])
def index(messages_type: Optional[str] = None):
    '''Login or Register as a user'''
    return render_template('index.html')


@app.route('/dashboard', methods=['GET'])
def dashboard():
    '''
    User dashboard route.

    If there is no user_id in session then redirect to the index route and flash error.
    Otherwise, render the dashboard template.
    '''
    if 'user_id' not in session:
        flash("Please login or register to enter the site.", 'dashboard_error')
        return redirect(url_for('index'))

    return render_template('dashboard.html')


@app.route('/register', methods=['POST'])
def register() -> Response:
    '''
    Register user route.

    Gets the input data from the form and validates it, if not valid, flashes error
    messages from the validate_user method in the User model, then redirects to the 
    index route. Otherwise, registers the user in the database and stores the user's 
    ID in session, then redirects to the dashboard.
    '''
    data: Dict[str, str] = dict(request.form)
    if not User.validate_user(data):
        print(f'''\n\n{'_'*80}\n\nUser Not Valid\n\n
            {'_'*80}'''
              )
        return redirect(url_for('index'))

    user_id: int = User.register_user(data)
    session['user_id'] = user_id
    return redirect("/dashboard")


@app.route('/login', methods=['POST'])
def login() -> Response:
    '''
    Login a user route.

    Checks for a user in the database with the input email and password. If the email
    is not in the database or the hashed_password doesn't match that user's password
    in the database, flashes error message and redirects to the index route. Otherwise,
    gets the user_id and stores it in session, then redirect to the dashboard.
    '''
    data: dict[str, str] = {"email": request.form["email"]}
    user_in_db: User | None = User.get_user_by_email(data)

    if not user_in_db or not User.check_password(user_in_db.password, request.form['password']):
        flash("Invalid Email and/or Password", 'login_error')
        return redirect(url_for('index'))

    user_id: int = user_in_db.id
    session['user_id'] = user_id
    return redirect("/dashboard")


@app.route('/logout', methods=['GET'])
def logout() -> Response:
    '''
    Logout route.

    Clears session and redirects to the index route.
    '''
    session.clear()
    return redirect("/")
