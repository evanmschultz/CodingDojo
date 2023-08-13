from flask_app import app
from flask_app.models.recipe_model.recipe import Recipe
from flask import render_template, request, redirect, session, flash, url_for

from datetime import datetime


@app.route("/recipes", methods=["GET"])
def recipes():
    """
    Displays the recipes page.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    If logged in, displays all the recipes with the first name of the user that created it.
    If the `user_id` in session matches the `user_id` from a recipe in the table, the `edit`
    and `delete` inputs will be available for that recipe; otherwise, only the `view` recipe
    link is displayed for that recipe.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    recipes: list[Recipe] = Recipe.get_all_recipes()

    user_id: int = session["user_id"]
    user_first_name: str = session["user_first_name"]
    user_data: dict = {"user_id": user_id, "user_first_name": user_first_name}

    return render_template("recipes.html", recipes=recipes, user_data=user_data)


@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def show_recipe(recipe_id: int):
    """
    Displays the details of a specific recipe.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    If logged in and the recipe exists, shows the recipe details.
    If the recipe does not exist, a flash message is displayed, and the user is redirected
    to the recipes page.

    Args:
        recipe_id (int): The ID of the recipe to be displayed.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    recipe: Recipe = Recipe.get_recipe_by_id(recipe_id)  # type: ignore

    formatted_date: str = format_date(recipe.date_made)
    recipe_date_made: str = formatted_date
    user_first_name: str = session["user_first_name"]

    if not recipe:
        flash("Recipe not found.", "recipe_error")
        return redirect(url_for("recipes"))
    """
    Add this code and add edit and delete buttons to show_recipe.html to allow user to 
    edit or delete recipe from this page if they are the author. Make sure to uncomment
    user_is_owner in the return statement below.
    
    # user_is_owner: bool = False
    # if recipe.user_id == session["user_id"]:
    #    user_is_owner = True
    """
    return render_template(
        "show_recipe.html",
        recipe=recipe,
        # user_is_owner=user_is_owner,
        recipe_date_made=recipe_date_made,
        user_first_name=user_first_name,
    )


@app.route("/recipes/add", methods=["GET"])
def add_recipe_page():
    """
    Displays create recipe page.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    If logged in, displays the create recipe form with fields: name (text), description (text_area),
    instructions (text_area), date made (date), and under 30 min (radial).
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    return render_template("create_recipe.html")


@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    """
    Processes the create recipe form.

    Validates the form data and creates a new recipe in the database if validation passes.
    Redirects to the show_recipe page for the created recipe upon successful creation,
    otherwise flashes errors and redirects back to the create page.

    Notes:
        under_30_min defaults to zero incase a user overrides the html `required` attribute.
    """
    recipe_data: dict = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30_min": request.form.get("under_30_min", default="0"),
        "user_id": session["user_id"],
        "creator_first_name": session["user_first_name"],
    }

    if not Recipe.validate_recipe(recipe_data):
        return redirect(url_for("add_recipe_page"))

    recipe_id = Recipe.add_recipe(recipe_data)

    return redirect(url_for("show_recipe", recipe_id=recipe_id))


@app.route("/recipes/<int:recipe_id>/edit", methods=["GET"])
def edit_recipe_page(recipe_id: int):
    """
    Displays edit recipe page.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    If logged in, displays edit recipe form with fields: name (text), description (text_area),
    instructions (text_area), date made (date), and under 30 min (radial) for the recipe
    identified by the given recipe_id.

    Args:
        recipe_id (int): The ID of the recipe to be displayed.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response
    recipe = Recipe.get_recipe_by_id(recipe_id)

    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/recipes/<int:recipe_id>/edit", methods=["POST"])
def edit_recipe(recipe_id: int):
    """
    Updates the recipe in the database.

    Checks if the logged-in user is the owner of the recipe and
    if the submitted data is valid according to the validation requirements.

    If the recipe does not exist, the user is not the owner, or the validation fails, an error
    message is flashed, and the user is redirected to the recipes page.

    If all checks pass, the recipe is updated with the new data, and the user is redirected to
    the recipes page.

    Notes:
        under_30_min defaults to zero incase a user overrides the html `required` attribute.
    """

    recipe = Recipe.get_recipe_by_id(recipe_id)

    if not recipe:
        flash("Cannot find recipe in the database", "recipe_error")
        return redirect(url_for("recipes"))

    if recipe and recipe.user_id == session.get("user_id"):
        recipe_data: dict = {
            "id": recipe_id,
            "name": request.form["name"],
            "description": request.form["description"],
            "instructions": request.form["instructions"],
            "date_made": request.form["date_made"],
            "under_30_min": request.form.get("under_30_min", default="0"),
        }

        if not Recipe.validate_recipe(recipe_data):
            return redirect(url_for("edit_recipe", recipe_id=recipe_id))

        Recipe.update_recipe(recipe_data)
    else:
        flash("You do not have permission to edit this recipe.", "recipe_error")
        return redirect(url_for("recipes"))

    return redirect(url_for("show_recipe", recipe_id=recipe_id))


@app.route("/recipes/<int:recipe_id>/delete", methods=["POST"])
def delete_recipe(recipe_id: int):
    """
    Deletes the recipe based on the id given.

    First, checks if the user is logged in by calling the `is_user_logged_in` function.
    If not logged in, flashes an error message and redirects to the login page.

    Checks if the logged-in user is the owner of the recipe. If not, flashes an error message and redirects.

    If all checks pass, deletes the recipe and redirects to the recipes page.

    Args:
        recipe_id (int): The ID of the recipe to be deleted.
    """
    logged_in, response = is_user_logged_in()
    if not logged_in:
        return response

    recipe = Recipe.get_recipe_by_id(recipe_id)

    if not recipe or recipe.user_id != session["user_id"]:
        flash("You do not have permission to delete this recipe.", "recipe_error")
        return redirect(url_for("recipes"))

    Recipe.delete_recipe(recipe_id)

    flash("Recipe deleted successfully.", "recipe_success")
    return redirect(url_for("recipes"))


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
        flash("Please login or register to enter the site.", "recipes_error")
        return False, redirect(url_for("login_page"))


def format_date(date_string: datetime) -> str:
    """
    Updates the date_made format for American readability.

    Converts date_string (yyyy-mm-dd) into a datetime object then reformats the object using
    datetime's strftime method returning a string in the format (Month Name dd, yyyy).

    Args:
        date_string (str): The date string to reformat.

    Returns:
        str: The reformatted date string.

    Example:
        2023-08-11 becomes August 11, 2023
    """
    # date_object: datetime = datetime.strptime(date_string, "%Y-%m-%d")

    date: str = date_string.strftime("%B %d, %Y")
    return date
