from flask_app import app

from flask import redirect, render_template, request, url_for
from werkzeug import Response
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


# Root Route
@app.route('/dojos', methods=['GET'])
def all_dojos() -> str:
    """Gets all the dojos and displays them on the page."""
    dojos: list[Dojo] = Dojo.get_dojos()
    print(f"\n{'_'*80}\n\n{dojos}\n{'_'*80}\n")

    return render_template('dojos.html', dojos=dojos, display_all=True)


# Add Dojo Route
@app.route('/create_dojo', methods=['POST'])
def create_dojo() -> Response:
    """Adds a dojo to the database from the user's input."""
    dojo_data: dict = request.form
    Dojo.create_dojo(dojo_data)

    return redirect('/dojos')


# Show Dojo
@app.route('/dojos/<int:dojo_id>', methods=['GET'])
def show_dojo(dojo_id: int) -> str:
    """
    Displays the dojo's information and its ninjas. 

    Conditionally displays dojo name edit form.
    """
    dojo: Dojo | None = Dojo.get_dojo(dojo_id)
    ninjas: list = Ninja.get_ninjas(dojo_id)

    if not dojo:
        print(
            f"\n\n{'_'*80}show_dojo:\n\nDojo.get_dojo() failed to get return Dojo.\n{'_'*80}")

    # Get the 'editing' parameter from the request's query parameters
    editing: bool = request.args.get(key='editing', default='False') == 'True'

    return render_template('dojos.html', dojo=dojo, ninjas=ninjas, editing=editing, display_all=False)


# Edit Dojo form
@app.route('/dojos/<int:dojo_id>/edit', methods=['GET'])
def update_dojo_route(dojo_id: int) -> Response:
    """Render the show_dojo route with the edit inputs."""
    return redirect(url_for('show_dojo', dojo_id=dojo_id, editing=True, display_all=False))


# Update Dojo Route
@app.route('/update_dojo', methods=['POST'])
def update_dojo() -> Response:
    """Updates a dojo in the database from the user's input"""
    dojo_data: dict = request.form
    dojo_id: int = Dojo.update_dojo(dojo_data)
    print(f"\n\n{'_'*80}\n\ndojo_data\n\n{dojo_data}\n{'_'*80}")

    return redirect(url_for('show_dojo', dojo_id=dojo_id, editing=False, display_all=False))


# Delete Dojo Route
@app.route('/delete_dojo', methods=['POST'])
def delete_dojo() -> Response:
    dojo_data: dict = request.form
    dojo_id: int = int(dojo_data['id'])
    Dojo.delete_dojo(dojo_id)

    return redirect('/dojos')
