import re
from flask import flash
# Database connection instance
from flask_app.config.mysql_connection import connectToMySQL
# Type hinting imports
from typing import Any, Dict, Literal, NoReturn, Self, Tuple, Union


class User:
    database: str = 'users'

    def __init__(self, data: dict) -> None:
        self.id: int = data['id']
        self.first_name: str = data['first_name']
        self.last_name: str = data['last_name']
        self.email: str = data['email']
        self.created_at: str = data['created_at']
        self.updated_at: str = data['updated_at']

    # READ Method

    @classmethod
    def get_all_users(cls) -> list[Self]:
        """
        Queries the 'users' table in the database and returns all records 
        as instances of the User class.

        Args:
            cls (class): The User class.

        Returns:
            list[Self]: A list of User instances populated with data from 
            the database.

        Notes:
            This is a class method for the User class.
        """

        # Set query
        query: str = 'SELECT * FROM users;'

        # Get users list from database
        results: tuple[dict[str, Any], ...] | Literal[False] = connectToMySQL(
            db=cls.database).query_db(query=query)  # type: ignore

        print(results)
        users = []
        if results:
            users: list[Self] = [cls(user) for user in results]

        return users

    # Read Method

    @classmethod
    def get_user_by_id(cls, user_id: int) -> Union['User', Literal[False]]:
        """
        Queries the 'users' table in the database and returns the one record
        where the id is equal to the 'user_id' arg as an instance of the User
        class.

        Args: 
            cls (class): The User Class
            user_id (int): The id of the user to be queried from the database.


        Returns:
            Self: An instance of the User class with self.id = user_id

        Notes:
            This is a class method for the User class.
        """

        # Set select query where id = user_id
        query: str = '''
                    SELECT * FROM users
                    WHERE id = %(id)s;
        '''

        # Set dictionary for data to be passed into the query
        data: dict[str, int] = {'id': user_id}
        # Run query method on database connection class
        results: list[dict[str, Any]] | Literal[False] = connectToMySQL(db=cls.database).query_db(
            query=query, data=data)  # type: ignore

        user_data: dict[str, Any] = {}
        if results:
            # Extract the user_data Dict from the results list
            user_data = results[0]
            ...
        else:
            # Handle the case where the query failed or returned no results
            print("No results found or the query failed.")

        try:
            # Try to instantiate the user and return the instance
            user: Self = cls(user_data)
            return user
        except Exception as e:
            # Print the exception of a user instance couldn't be created and return nothing
            print(f"Failed to create user: {e}")
            return False

    # Create Method

    @classmethod
    def create_user(cls, user_data: dict[str, Any]) -> int | Literal[False]:
        """
        Queries the 'users' table in the database to create a row with the
        user input data

        Args: 
            cls (class): The User Class
            user_data (dict): A dictionary holding all the user input data

        Returns:
            None | False: Returns nothing if successful, or False and prints the error if it failed

        Notes:
            This is a class method for the User class.
        """

        # Set query to insert row into users table in the database
        query: str = '''
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
        '''

        # Call connection method and query the database to create user and store result as a variable
        result: int | Literal[False] = connectToMySQL(
            db=cls.database).query_db(query=query, data=user_data)  # type: ignore

        return result

    # Update User Method

    @classmethod
    def update_user(cls, user_data: dict[str, Any]) -> NoReturn | Literal[False]:
        """
        Updates the user in the database


        Args:
            cls (class): The User class.
            user_data (dict): A dictionary holding all the user input data.

        Returns:
            None | False: Returns nothing if successful, or False and prints the error if it failed.

        Notes:
            This is a class method for the User class.
        """

        # Set query to insert row into users table in the database
        query: str = '''
                UPDATE users
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(id)s;
        '''

        # Call connection method and query the database to create user and store result as a variable
        result: NoReturn | Literal[False] = connectToMySQL(
            db=cls.database).query_db(query=query, data=user_data)  # type: ignore

        return result

    # Delete User Method

    @classmethod
    def delete_user(cls, user_id: int) -> NoReturn | Literal[False]:
        """
        Deletes the user from the database.

        Args:
            cls (class): The User class.
            user_id (int): The id of the user to delete from the database.

        Returns:
            NoReturn: If successful nothing is returned.
            False: If the query fails False is returned and the error message is printed.

        Notes:
            This is a class method for the User class.
        """

        query: str = '''
                    DELETE FROM users
                    WHERE id = %(id)s;
        '''
        data: dict[str, int] = {'id': user_id}

        results: NoReturn | Literal[False] = connectToMySQL(
            db=cls.database).query_db(query=query, data=data)  # type: ignore

        return results

    @staticmethod
    def validate_user(user_data: Dict) -> bool:
        """
        Validates user inputs.

        Args:
            user_data (Dict): The user_data from the input form.
                {'first_name': str, 'last_name': str, 'email': str}

        Returns:
            boolean: True if validation checks pass, False otherwise.

        Raises:
            Flash messages
        """
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        is_valid = True
        if len(user_data['first_name']) < 1:
            flash("First Name must be at least 1 character long.", 'error')
            is_valid = False
        if len(user_data['last_name']) < 1:
            flash("Last Name must be at least 1 character long.", 'error')
            is_valid = False
        if not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid email address!", 'error')
            is_valid = False
        return is_valid
