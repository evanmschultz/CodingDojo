from flask_app import app

from typing import Literal
from flask import redirect, render_template, request, url_for
from werkzeug import Response
from flask_app.models.dojo import Dojo


# Root Route
@app.route('/dojos', methods=['GET'])
def all_users() -> str:
    """Gets all the users and displays them on the page."""
    dojos: list[Dojo] = Dojo.get_dojos()
    print(f"\n{'_'*80}\n\n{dojos}\n{'_'*80}\n")

    return render_template(template_name_or_list='dojos.html', dojos=dojos)

# Add Dojo Route


@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    """Adds a dojo to the database from the user's input."""
    dojo_data: dict = request.form
    Dojo.create_dojo(dojo_data)

    return redirect('/')
