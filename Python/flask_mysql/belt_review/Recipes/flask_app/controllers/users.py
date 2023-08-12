from flask_app import app

from flask_app.models.user_model.user import User
from flask import render_template, request, redirect, session, flash, url_for


@app.route("/", methods=["GET"])
def login_page():
    """Login or Register as a user"""
    return render_template("login_page.html")


@app.route("/register", methods=["POST"])
def register():
    """
    Register user route.

    Gets the input data from the form and validates it, if not valid, flashes error
    messages from the validate_user method in the User model, then redirects to the
    login_page route. Otherwise, registers the user in the database and stores the user's
    ID in session, then redirects to the recipes.
    """
    data: dict = dict(request.form)
    if not User.validate_user(data):
        print(
            f"""\n\n{'_'*80}\n\nUser Not Valid\n\n
            {'_'*80}"""
        )
        return redirect(url_for("login_page"))

    user_id: int = User.register_user(data)
    session["user_id"] = user_id
    return redirect("/recipes")


@app.route("/login", methods=["POST"])
def login():
    """
    Login a user route.

    Checks for a user in the database with the input email and password. If the email
    is not in the database or the hashed_password doesn't match that user's password
    in the database, flashes error message and redirects to the login_page route. Otherwise,
    gets the user_id and stores it in session, then redirect to the recipes.
    """
    data: dict = {"email": request.form["email"]}
    user_in_db: User | None = User.get_user_by_email(data)

    if not user_in_db or not User.check_password(
        user_in_db.password, request.form["password"]
    ):
        flash("Invalid Email and/or Password", "login_error")
        return redirect(url_for("login_page"))

    user_id: int = user_in_db.id
    session["user_id"] = user_id
    return redirect("/recipes")


@app.route("/logout", methods=["GET"])
def logout():
    """
    Logout route.

    Clears session and redirects to the login_page route.
    """
    session.clear()
    return redirect("/")
