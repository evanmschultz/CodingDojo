from typing import Optional
from flask import flash
from pydantic import ValidationError
from flask_app.config.mySQLConnection import connectToMySQL
from flask_app.models.recipe_model.recipe_validation import RecipeData

# Type hinting import
from datetime import datetime


class Recipe:
    """The Recipe class"""

    database: str = "recipes"

    def __init__(self, recipe_data: dict) -> None:
        """Instantiates a Recipe instance"""
        self.id: int = recipe_data["id"]
        self.name: str = recipe_data["name"]
        self.description: str = recipe_data["description"]
        self.instructions: str = recipe_data["instructions"]
        self.date_made: datetime = recipe_data["date_made"]
        self.under_30_min: int = recipe_data["under_30_min"]
        self.created_at: datetime = recipe_data["created_at"]
        self.updated_at: datetime = recipe_data["updated_at"]
        self.user_id: int = recipe_data["user_id"]
        self.creator_first_name: str = recipe_data["first_name"]

    @classmethod
    def get_all_recipes(cls) -> list["Recipe"]:
        """
        Gets all the recipes from the database including the name from the row in the
        users table where the users.id matches the user_id.

        Returns:
            list: A list of instances of the recipe class.
        """
        query: str = """
                    SELECT recipes.*, users.first_name
                    FROM recipes
                    LEFT JOIN users ON users.id = recipes.user_id;
        """
        # To get all of the user's information change the query to be:
        """
        SELECT * FROM recipes
        LEFT JOIN users ON users.id = recipes.user_id;
        """
        results: tuple[dict] = connectToMySQL(cls.database).select_from_db(query)

        recipes = []
        if results:
            recipes: list[Recipe] = [cls(recipe) for recipe in results]

        return recipes

    @classmethod
    def get_recipe_by_id(cls, recipe_id: int) -> Optional["Recipe"]:
        """
        Gets a single recipe from the database by its ID, including the name from the row in the
        users table where the users.id matches the user_id.

        Args:
            recipe_id (int): The ID of the recipe to retrieve.

        Returns:
            Recipe: An instance of the Recipe class, or None if not found.
        """
        query: str = """
                    SELECT recipes.*, users.first_name
                    FROM recipes
                    LEFT JOIN users ON users.id = recipes.user_id
                    WHERE recipes.id = %(id)s;
        """
        data: dict = {"id": recipe_id}
        results: tuple[dict] = connectToMySQL(cls.database).select_from_db(query, data)

        recipe = None
        if results:
            recipe: Optional[Recipe] = cls(results[0])

        return recipe

    @classmethod
    def add_recipe(cls, recipe_data: dict) -> int:
        """
        Adds a recipe to the database.

        Args:
            recipe_data (dict): The recipe data, including:
                {
                    'name': str,
                    'description': str,
                    'instructions': str,
                    'date_made': str (yyyy-mm-dd),
                    'under_30_min': int (0 or 1)
                    'user_id': int
                }

        Returns:
            int: The ID of the created recipe.
        """
        query: str = """
                    INSERT INTO recipes (name, description, instructions, date_made, under_30_min, user_id)
                    VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30_min)s, %(user_id)s);
        """

        recipe_id: int = connectToMySQL(cls.database).insert_into_db(query, recipe_data)
        return recipe_id

    @classmethod
    def update_recipe(cls, recipe_data: dict) -> int:
        """
        Updates the recipe in the database

        Args:
            recipe_data (dict): A dictionary holding all the updated data.
                {
                    'id': int,
                    'name': str,
                    'description': str,
                    'instructions': str,
                    'date_made': str (yyyy-mm-dd),
                    'under_30_min': int (0 or 1)
                }

        Returns:
            int: Returns the row_id of the updated recipe.
        """
        query: str = """
                    UPDATE recipes
                    SET name = %(name)s, description = %(description)s, instructions = %(instructions)s,
                    date_made = %(date_made)s, under_30_min = %(under_30_min)s
                    WHERE id = %(id)s;
        """
        recipe_id: int = connectToMySQL(db=cls.database).update_db(
            query=query, data=recipe_data
        )

        return recipe_id

    @classmethod
    def delete_recipe(cls, recipe_id: int) -> None:
        """
        Deletes the recipe from the database.

        Args:
            recipe_id (int): The id of the recipe to delete from the database.
        """
        query: str = """
                    DELETE FROM recipes
                    WHERE id = %(id)s;
        """
        data: dict = {"id": recipe_id}

        connectToMySQL(db=cls.database).delete_from_db(query=query, data=data)

    @staticmethod
    def validate_recipe(recipe_data: dict) -> bool:
        """
        Validates recipe inputs using the Pydantic schema in the RecipeData class.

        Args:
            recipe_data (dict): The recipe_data from the input form.
                {
                    'name': str,
                    'description': str,
                    'instructions': str,
                    'date_made': str (yyyy, mm, dd),
                    'under_30_min': int (0, 1) # Indicates True or False
                }

        Returns:
            boolean: True if validation checks pass, False otherwise.

        Raises:
            Flash messages constructed from the ValueErrors in the RecipeData class.
        """
        try:
            print(
                f"""\n\n{'_'*80}\n\nRecipe date_made\n\n
                {recipe_data['date_made']}\n{'_'*80}"""
            )
            RecipeData(**recipe_data)
            return True
        except ValidationError as e:
            print("Validation Error:", e)
            for error in e.errors():
                flash(f"{error['msg'].strip('Value error, ')}", "recipe_error")
            return False
