from typing import Literal
from flask import Flask, redirect, render_template, request, url_for
from werkzeug import Response
from user import User


app = Flask(import_name=__name__)


# Root Route
@app.route(rule='/', methods=['GET'])
def all_users() -> str:
    """
    Gets all the users and displays them on the page
    """

    users: list[User] = User.get_all_users()
    print(f"\n{'_'*80}\n\n{users}\n{'_'*80}\n")

    return render_template(template_name_or_list='all_users.jinja2', users=users)


# Create User Display Form Route
@app.route(rule='/add_user', methods=['GET'])
def add_user() -> str:
    return render_template(template_name_or_list='add_user.jinja2')


# Create User POST Route
@app.route(rule='/create_user', methods=['POST'])
def create_user() -> Response:
    # Create a dict from request.form (make sure the keys lineup perfectly with the query in create_user())
    user_data: dict[str, str] = request.form

    # Call the class method create_user() with the input data
    User.create_user(user_data=user_data)\

    # Redirect to the index page
    return redirect(location='/')


# Show User Route
@app.route(rule='/user/<int:user_id>', methods=['GET'])
def show_user(user_id) -> str:
    user: User | Literal[False] = User.get_user_by_id(user_id=user_id)

    if not user:
        print(
            f"\n\n{'_'*80}show_user:\n\nUser.get_user_by_id() returned False\n{'_'*80}")

    return render_template(template_name_or_list='user.jinja2', user=user, editing=False)


# Edit User Form Route
@app.route(rule='/edit_user/<int:user_id>', methods=['GET'])
def edit_user_display(user_id) -> str:
    user: User | Literal[False] = User.get_user_by_id(user_id=user_id)

    if not user:
        print(
            f"\n\n{'_'*80}edit_user_display:\n\nUser.get_user_by_id() returned False\n{'_'*80}")

    return render_template(template_name_or_list='user.jinja2', user=user, editing=True)


# Update User Route
@app.route(rule='/update_user', methods=['POST'])
def update_user() -> Response:
    user_data: dict[str, str] = request.form

    User.update_user(user_data=user_data)

    return redirect(location=url_for(endpoint='show_user', user_id=user_data['id']))


# Delete User Route
@app.route(rule="/delete_user/<int:user_id>", methods=['POST'])
def delete_user_route(user_id) -> Response:
    User.delete_user(user_id=user_id)

    return redirect(location="/")


if __name__ == "__main__":
    app.run(debug=True)
