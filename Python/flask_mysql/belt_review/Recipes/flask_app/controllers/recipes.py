from flask_app import app

from flask_app.models.recipe_model.recipe import Recipe
from flask import render_template, request, redirect, session, flash, url_for


@app.route("/recipes", methods=["GET"])
def recipes():
    """
    Recipes route.

    Displays all the recipes with the first name of the user that created it. If the `id` in
    session matches the `user_id` from the the recipe, the `edit` and `delete` inputs
    will be available, otherwise it only displays `view` recipe link.
    """
    if "user_id" not in session:
        flash("Please login or register to enter the site.", "recipes_error")
        return redirect(url_for("login_page"))

    return render_template("recipes.html")
