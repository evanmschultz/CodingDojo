# TODO: PASSWORD_REGEX

from flask_app import app
from flask_app.config.mySQLConnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
import re

# Type hinting and pretty print imports
from typing import Dict, Optional, Tuple
from datetime import datetime


class User:
    bcrypt = Bcrypt()  # You can initialize Bcrypt without the app object
    database: str = 'user_logins'

    def __init__(self, user_data: Dict) -> None:
        """Instantiates a User instance"""
        self.id: int = user_data['id']
        self.first_name: str = user_data['first_name']
        self.last_name: str = user_data['last_name']
        self.email: str = user_data['email']
        self.password: str = user_data['password']
        self.created_at: datetime = user_data['created_at']
        self.updated_at: datetime = user_data['updated_at']

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes the user's password.

        Args:
            password (str): The user's raw password.

        Returns:
            hashed_password (str): The hash created from the password.
        """
        hashed_password: str = User.bcrypt.generate_password_hash(
            password).decode('utf-8')
        return hashed_password

    @staticmethod
    def check_password(hashed_password: str, password: str) -> bool:
        """
        Checks the user input password against the hashed password in the database.

        Args:
            password (str): The user's raw password.

        Returns:
            hashed_password (str): The hash created from the password.
        """
        valid_password: bool = User.bcrypt.check_password_hash(
            hashed_password, password)
        return valid_password

    @classmethod
    def get_user_by_email(cls, data):
        """
        Gets a user from the database using email.

        Args:
            email (str): The user's email.

        Returns:
            user (User): An instance of the User class.
        """
        query: str = '''
                    SELECT * FROM users
                    WHERE email = %(email)s;
        '''
        results: Tuple[Dict] = connectToMySQL(
            cls.database).select_from_db(query, data)

        user_data: Dict = {}
        if results:
            user_data = results[0]

        user = None
        if len(user_data) > 1:
            user: Optional[User] = cls(user_data)

        return user

    @classmethod
    def register_user(cls, data: Dict) -> int:
        """
        Creates a user in the database.

        Hashes the the user's password. Updates the data dictionary with the hashed
        password. Then inserts all the user's information into the database.

        Args:
            password (str): The user's raw password.

        Returns:
            user_id (int): The ID of the created user.
        """
        hashed_password: str = User.hash_password(data['password'])
        data['password'] = hashed_password

        query: str = '''
                    INSERT INTO users (first_name, last_name, email, password) 
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        '''

        user_id: int = connectToMySQL(cls.database).insert_into_db(query, data)
        return user_id

    @staticmethod
    def validate_user(user_data: Dict) -> bool:
        """
        Validates user inputs.

        first_name: Must be length of at least 1.
        last_name: must be length of at least 1.
        email: Must be a valid email address.
        password: Must have at least one of each, lowercase letter, uppercase letter,
            number, and special character, as well as be at least 8 characters long.
        confirm_password: Must match password.

        Args:
            user_data (Dict): The user_data from the input form:
                {
                    'first_name': str, 
                    'last_name': str, 
                    'email': str, 
                    'password': str, 
                    'confirm_password': str
                }

        Returns:
            boolean: True if validation checks pass, False otherwise.

        Raises:
            Flash messages
        """
        EMAIL_REGEX: re.Pattern[str] = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        '''Password requirements (at least one of each): [a-z] (lowercase), [A-Z] (uppercase)
            [0-9] (numeric), (\\W) (non-alphanumeric)'''
        PASSWORD_REGEX: re.Pattern[str] = re.compile(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).+$')

        is_valid: bool = True

        # First Name
        if len(user_data['first_name'].strip()) < 1:
            flash("First Name must be at least 1 character long.", 'register_error')
            is_valid = False

        # Last Name
        if len(user_data['last_name'].strip()) < 1:
            flash("Last Name must be at least 1 character long.", 'register_error')
            is_valid = False

        # Email
        if not EMAIL_REGEX.match(user_data['email'].strip()):
            flash("Invalid email address!", 'register_error')
            is_valid = False

        # Password Length
        if not len(user_data['password'].strip()) >= 8:
            flash("Password must be at least 8 characters long!", 'register_error')
            is_valid = False

        # Password Regex
        if not PASSWORD_REGEX.match(user_data['password']):
            flash('''
                    Password must contain at least 1 of each of the following: \n
                    lowercase letter, uppercase letter, number, and special character''',
                  'register_error')
            is_valid = False

        # Password Match
        if not user_data['password'].strip() == user_data['confirm_password'].strip():
            flash("Passwords must match!", 'register_error')
            is_valid = False

        return is_valid
