from flask_app import app

from flask import redirect, render_template, request, url_for
from werkzeug import Response
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


# Ninja Route
@app.route('/ninja', methods=['GET'])
@app.route('/ninja/<int:dojo_id>', methods=['GET'])
@app.route('/ninja/<int:ninja_id>/dojo/<int:dojo_id>', methods=['GET'])
def display_ninja(ninja_id: int | None = None, dojo_id: int | None = None) -> str:
    dojos: list = Dojo.get_dojos()
    ninja: Ninja | None = Ninja.get_ninja(ninja_id) if ninja_id else None
    print(f"\n\n{'_'*80}\n\nNinja\n\n{ninja}\n\n{'_'*80}")

    if ninja_id and not ninja:
        print(
            f"\n\n{'_'*80}show_ninja:\n\nNinja.get_ninja() failed to get return Ninja.\n{'_'*80}")

    # Get the 'editing' parameter from the request's query parameters
    editing: bool = request.args.get(key='editing', default='False') == 'True'

    return render_template('ninja.html', ninja=ninja, dojos=dojos, editing=editing, dojo_id=dojo_id)


# Add Ninja Route
@app.route('/create_ninja', methods=['POST'])
def create_ninja() -> Response:
    """Adds a ninja to the database with the ninja_id as dojo_id."""
    ninja_data: dict = request.form
    print(f"\n\n{'_'*80}\n\n{ninja_data}\n\nDojo\n{'_'*80}")
    Ninja.create_ninja(ninja_data)

    dojo_id: int = int(ninja_data['dojo_id'])

    return redirect(url_for('show_dojo', dojo_id=dojo_id))


# Update Ninja Route
@app.route('/ninja/<int:ninja_id>/update', methods=['POST'])
def update_ninja(ninja_id: int) -> Response:
    """Update a ninja's information."""
    ninja_data: dict[str, int | str] = dict(request.form)
    print(f"\n\n{'_'*80}\n\nninja_data\n\n{ninja_data}\n{'_'*80}")
    ninja_data['id'] = ninja_id
    dojo_id: int = int(ninja_data['dojo_id'])

    Ninja.update_ninja(ninja_data)

    return redirect(url_for('show_dojo', dojo_id=dojo_id))


# Delete Dojo Route
@app.route('/delete_dojo', methods=['POST'])
def delete_ninja() -> Response:
    dojo_data: dict = request.form
    dojo_id: int = int(dojo_data['id'])
    Dojo.delete_dojo(dojo_id)

    return redirect('/dojos')
