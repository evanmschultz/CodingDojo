from flask import flash
from flask_bcrypt import Bcrypt
from pydantic import ValidationError
from flask_app.config.mySQLConnection import connectToMySQL
from flask_app.models.user_model.user_validation import UserData

# Type hinting imports
from typing import Optional
from datetime import datetime


class User:
    """The User class"""

    bcrypt = Bcrypt()
    database: str = "tv_shows"

    def __init__(self, user_data: dict) -> None:
        """Instantiates a User instance"""
        self.id: int = user_data["id"]
        self.first_name: str = user_data["first_name"]
        self.last_name: str = user_data["last_name"]
        self.email: str = user_data["email"]
        self.password: str = user_data["password"]
        self.created_at: datetime = user_data["created_at"]
        self.updated_at: datetime = user_data["updated_at"]

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes the user's password.

        Args:
            password (str): The user's raw password.

        Returns:
            str: The hash created from the password.
        """
        hashed_password: str = User.bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )
        return hashed_password

    @staticmethod
    def check_password(hashed_password: str, input_password: str) -> bool:
        """
        Checks the user input password against the hashed password in the database.

        Args:
            password (str): The user's raw password.

        Returns:
            bool: True if the input_password matches the password
            in the database and False if not.
        """
        correct_password: bool = User.bcrypt.check_password_hash(
            hashed_password, input_password
        )
        return correct_password

    @classmethod
    def get_user_by_email(cls, data):
        """
        Gets a user from the database using email.

        Args:
            email (str): The user's email.

        Returns:
            User: An instance of the User class.
        """
        query: str = """
                    SELECT * FROM users
                    WHERE email = %(email)s;
        """
        results: tuple[dict] = connectToMySQL(cls.database).select_from_db(query, data)

        user_data: dict = {}
        if results:
            user_data = results[0]

        user = None
        if len(user_data) > 1:
            user: Optional[User] = cls(user_data)

        return user

    @classmethod
    def get_user_by_id(cls, user_id: int) -> Optional["User"]:
        """
        Gets a user from the database using the user ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Optional[User]: An instance of the User class if found, None otherwise.
        """
        query: str = """
                    SELECT * FROM users
                    WHERE id = %(user_id)s;
        """
        results: tuple[dict] = connectToMySQL(cls.database).select_from_db(
            query, {"user_id": user_id}
        )

        user_data: dict = {}
        if results:
            user_data = results[0]

        user = None
        if len(user_data) > 1:
            user = cls(user_data)

        return user

    @classmethod
    def register_user(cls, data: dict) -> int:
        """
        Creates a user in the database.

        Hashes the the user's password. Updates the data dictionary with the hashed
        password. Then inserts all the user's information into the database.

        Args:
            password (str): The user's raw password.

        Returns:
            int: The ID of the created user.
        """
        hashed_password: str = User.hash_password(data["password"])
        data["password"] = hashed_password

        query: str = """
                    INSERT INTO users (first_name, last_name, email, password) 
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """

        user_id: int = connectToMySQL(cls.database).insert_into_db(query, data)
        return user_id

    @staticmethod
    def validate_user(user_data: dict) -> bool:
        """
        Validates user inputs using the Pydantic schema in the user_validation model and
        checks for email uniqueness.

        1. Extracts the email from the user_data.
        1. Validates the user_data using the Pydantic schema (UserData) and captures
        any validation errors.
        1. If validation errors are found, stores messages in flash_messages list and sets validation_passed
        to False.
        1. Checks if the email already exists in the database, if it does, appends a flash message to the
        flash_messages list and sets validation_passed to False.
        1. Runs loop to get set all flash messages from flash_messages list.

        If there were no validation errors, returns True.

        Args:
            user_data (dict): The user_data from the input form. Contains:
                {
                    'first_name': str,
                    'last_name': str,
                    'email': str,
                    'password': str,
                    'confirm_password': str
                }

        Returns:
            bool: True if validation checks pass and email is unique, False otherwise.

        Raises:
            Flash Message: ValueErrors from the UserData class and a message if
                email already exists.
        """
        user_email: str = user_data["email"]
        data: dict = {"email": user_email}
        validation_passed = True
        flash_messages = []

        try:
            UserData(**user_data)
        except ValidationError as e:
            validation_passed = False

            for error in e.errors():
                if error["loc"][0] == "email":
                    flash_messages.append("Invalid email address.")
                else:
                    flash_messages.append(f"{error['msg'].strip('Value Error, ')}")

        if User.get_user_by_email(data):
            validation_passed = False
            flash_messages.append(
                "Email already exists. Login or use a different email."
            )

        for message in flash_messages:
            flash(message, "register_error")

        return validation_passed
