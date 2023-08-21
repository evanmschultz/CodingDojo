from flask_app import app
from flask_app.models.tv_show_model.tv_show import TV_Show
from flask import render_template, request, redirect, session, flash, url_for

from datetime import datetime


@app.route("/tv_shows", methods=["GET"])
def tv_shows():
    """
    Displays the tv_shows page.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    If logged in, displays all the tv_shows with the first name of the user that created it.
    If the `user_id` in session matches the `user_id` from a tv_show in the table, the `edit`
    and `delete` inputs will be available for that tv_show; otherwise, only the `view` tv_show
    link is displayed for that tv_show.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    tv_shows: list[TV_Show] = TV_Show.get_all_tv_shows()

    for tv_show in tv_shows:
        tv_show.release_date: str = format_date(tv_show.release_date)  # type: ignore

    user_id: int = session["user_id"]
    user_first_name: str = session["user_first_name"]
    user_data: dict = {"user_id": user_id, "user_first_name": user_first_name}
    print(
        f"""\n\n{'_'*80}\n\nuser_data\n\n
        {user_data}\n{'_'*80}"""
    )

    return render_template("tv_shows.html", tv_shows=tv_shows, user_data=user_data)


@app.route("/tv_shows/<int:tv_show_id>", methods=["GET"])
def show_tv_show(tv_show_id: int):
    """
    Displays the details of a specific tv_show.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    If logged in and the tv_show exists, shows the tv_show details.
    If the tv_show does not exist, a flash message is displayed, and the user is redirected
    to the tv_shows page.

    Args:
        tv_show_id (int): The ID of the tv_show to be displayed.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    tv_show: TV_Show = TV_Show.get_tv_show_by_id(tv_show_id)  # type: ignore

    formatted_date: str = format_date(tv_show.release_date) # type: ignore
    tv_show_release_date: str = formatted_date
    user_first_name: str = session["user_first_name"]

    if not tv_show:
        flash("TV_Show not found.", "tv_show_error")
        return redirect(url_for("tv_shows"))
    """
    Add this code and add edit and delete buttons to show_tv_show.html to allow user to 
    edit or delete tv_show from this page if they are the author. Make sure to uncomment
    user_is_owner in the return statement below.
    
    # user_is_owner: bool = False
    # if tv_show.user_id == session["user_id"]:
    #    user_is_owner = True
    """
    return render_template(
        "show_tv_show.html",
        tv_show=tv_show,
        # user_is_owner=user_is_owner,
        tv_show_release_date=tv_show_release_date,
        user_first_name=user_first_name,
    )


@app.route("/tv_shows/add", methods=["GET"])
def add_tv_show_page():
    """
    Displays create tv_show page.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    If logged in, displays the create tv_show form with fields: name (text), description (text_area),
    instructions (text_area), date made (date), and under 30 min (radial).
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    return render_template("add_tv_show.html")


@app.route("/add_tv_show", methods=["POST"])
def add_tv_show():
    """
    Processes the create tv_show form.

    Validates the form data and creates a new tv_show in the database if validation passes.
    Redirects to the show_tv_show page for the created tv_show upon successful creation,
    otherwise flashes errors and redirects back to the create page.

    Notes:
        under_30_min defaults to zero incase a user overrides the html `required` attribute.
    """
    tv_show_data: dict = {
        "title": request.form["title"],
        "description": request.form["description"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "user_id": session["user_id"],
    }

    if not TV_Show.validate_tv_show(tv_show_data):
        return redirect(url_for("add_tv_show_page"))

    tv_show_id: int = TV_Show.add_tv_show(tv_show_data)

    return redirect(url_for("tv_shows"))


@app.route("/tv_shows/<int:tv_show_id>/edit", methods=["GET"])
def edit_tv_show_page(tv_show_id: int):
    """
    Displays edit tv_show page.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    If logged in, displays edit tv_show form with fields: name (text), description (text_area),
    instructions (text_area), date made (date), and under 30 min (radial) for the tv_show
    identified by the given tv_show_id.

    Args:
        tv_show_id (int): The ID of the tv_show to be displayed.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response
    tv_show = TV_Show.get_tv_show_by_id(tv_show_id)

    return render_template("edit_tv_show.html", tv_show=tv_show)


@app.route("/tv_shows/<int:tv_show_id>/edit", methods=["POST"])
def edit_tv_show(tv_show_id: int):
    """
    Updates the tv_show in the database.

    Checks if the logged-in user is the owner of the tv_show and
    if the submitted data is valid according to the validation requirements.

    If the tv_show does not exist, the user is not the owner, or the validation fails, an error
    message is flashed, and the user is redirected to the tv_shows page.

    If all checks pass, the tv_show is updated with the new data, and the user is redirected to
    the tv_shows page.

    Notes:
        under_30_min defaults to zero incase a user overrides the html `required` attribute.
    """

    tv_show = TV_Show.get_tv_show_by_id(tv_show_id)

    if not tv_show:
        flash("Cannot find tv_show in the database", "tv_show_error")
        return redirect(url_for("tv_shows"))

    if tv_show and tv_show.user_id == session.get("user_id"):
        tv_show_data: dict = {
            "id": tv_show_id,
            "title": request.form["title"],
            "description": request.form["description"],
            "network": request.form["network"],
            "release_date": request.form["release_date"],
            "user_id": session["user_id"],
        }

        if not TV_Show.validate_tv_show(tv_show_data):
            return redirect(url_for("edit_tv_show", tv_show_id=tv_show_id))

        TV_Show.update_tv_show(tv_show_data)
    else:
        flash("You do not have permission to edit this tv_show.", "tv_show_error")
        return redirect(url_for("tv_shows"))

    return redirect(url_for("show_tv_show", tv_show_id=tv_show_id))


@app.route("/tv_shows/<int:tv_show_id>/delete", methods=["POST"])
def delete_tv_show(tv_show_id: int):
    """
    Deletes the tv_show based on the id given.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    Checks if the logged-in user is the owner of the tv_show. If not, flashes an error message and redirects.

    If all checks pass, deletes the tv_show and redirects to the tv_shows page.

    Args:
        tv_show_id (int): The ID of the tv_show to be deleted.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    tv_show = TV_Show.get_tv_show_by_id(tv_show_id)

    if not tv_show or tv_show.user_id != session["user_id"]:
        flash("You do not have permission to delete this tv_show.", "tv_show_error")
        return redirect(url_for("tv_shows"))

    TV_Show.delete_tv_show(tv_show_id)

    flash("TV_Show deleted successfully.", "tv_show_success")
    return redirect(url_for("tv_shows"))


@app.route("/tv_shows/<int:tv_show_id>/like", methods=["POST"])
def like_tv_show(tv_show_id: int):
    """
    Likes the TV show identified by the given tv_show_id for the logged-in user.

    Args:
        tv_show_id (int): The ID of the TV show to be liked.

    Returns:
        redirect: Redirects to the TV shows page.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    user_id: int = session["user_id"]
    TV_Show.like_tv_show(user_id, tv_show_id)

    flash("TV Show liked successfully.", "tv_show_success")
    return redirect(url_for("tv_shows", tv_show_id=tv_show_id))


@app.route("/tv_shows/<int:tv_show_id>/unlike", methods=["POST"])
def unlike_tv_show(tv_show_id: int):
    """
    Unlikes the TV show identified by the given tv_show_id for the logged-in user.

    Args:
        tv_show_id (int): The ID of the TV show to be unliked.

    Returns:
        redirect: Redirects to the TV shows page.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    user_id: int = session["user_id"]
    TV_Show.unlike_tv_show(user_id, tv_show_id)

    flash("TV Show unliked successfully.", "tv_show_success")
    return redirect(url_for("tv_shows", tv_show_id=tv_show_id))


def is_user_logged_in() -> tuple:
    """
    Checks if a user is logged in by verifying if "user_id" exists in the session.

    If the user is logged in ("user_id" exists in the session), returns a tuple with
    True and None. If the user is not logged in, flashes an error message and returns a tuple
    with False and a redirection to the login page.

    Returns:
        tuple: A tuple containing a boolean value representing whether the user is logged in,
               and either None (if logged in) or a redirect response (if not logged in).
    """
    if "user_id" in session:
        return True, None
    else:
        flash("Please login or register to enter the site.", "login_error")
        return False, redirect(url_for("login_page"))


def format_date(date_string: datetime) -> str:
    """
    Updates the release_date format for American readability.

    Converts date_string (yyyy-mm-dd) into a datetime object then reformats the object using
    datetime's strftime method returning a string in the format (Month Name dd, yyyy).

    Args:
        date_string (str): The date string to reformat.

    Returns:
        str: The reformatted date string.

    Example:
        2023-08-11 becomes August 11, 2023
    """

    date: str = date_string.strftime("%B %d, %Y")
    return date
