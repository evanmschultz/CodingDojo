from flask import Flask, Response, redirect, render_template, request
from user import User


app = Flask(import_name=__name__)


@app.route(rule='/', methods=['GET'])
def all_users() -> str:
    """
    Gets all the users and displays them on the page
    """

    users: list[User] = User.get_all_users()
    print(f"\n{'_'*80}\n\n{users}\n{'_'*80}\n")

    return render_template(template_name_or_list='all_users.jinja2', users=users)


@app.route(rule='/add_user', methods=['GET'])
def add_user() -> str:
    return render_template(template_name_or_list='add_user.jinja2')


@app.route(rule='/create_user', methods=['POST'])
def create_user() -> Response:
    # Create a dict from request.form (make sure the keys lineup perfectly with the query in create_user())
    user_data: dict[str, str] = request.form

    # Call the class method create_user() with the input data
    User.create_user(user_data=user_data)\

    # Redirect to the index page
    return redirect(location='/')


if __name__ == "__main__":
    app.run(debug=True)
