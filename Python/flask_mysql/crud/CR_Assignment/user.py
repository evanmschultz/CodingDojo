import datetime
# Database connection instance
from mysql_connection import connectToMySQL
# Type hinting imports
from typing import Any, Dict, Literal, NoReturn, Self, Tuple, Union


class User:
    db = 'users'

    def __init__(self, data) -> None:
        self.first_name: str = data['first_name']
        self.last_name: str = data['last_name']
        self.email: str = data['email']
        self.created_at: datetime = data['created_at']
        self.updated_at: datetime = data['updated_at']

    # READ Method

    @classmethod
    def get_all_users(cls) -> list[Self]:
        """
        Queries the 'users' table in the database and returns all records 
        as instances of the User class.

        Args:
            cls: The User class.

        Returns:
            list[Self]: A list of User instances populated with data from 
            the database.
        """

        # Set query
        query: str = 'SELECT * FROM users'

        # Get users list from database
        results: int | tuple[dict[str, Any], ...] | Literal[False] | None = connectToMySQL(
            db=cls.db).query_db(query=query)

        print(results)
        users = [cls(user) for user in results]

        return users

    # Read Method

    @classmethod
    def get_user(cls, user_id: int) -> Union['User', bool]:
        """
        Queries the 'users' table in the database and returns the one record
        where the id is equal to the 'user_id' arg as an instance of the User
        class.

        Args: 
            cls: The User Class
            user_id: An integer representing the id of the user being queried

        Returns:
            Self: An instance of the User class with self.id = user_id
        """

        # Set select query where id = user_id
        query: str = '''
                    SELECT * FROM users
                    WHERE id = %(user_id)s
                    '''

        # Set dictionary for data to be passed into the query
        user_id: dict[str, int] = {'id': user_id}
        # Run query method on database connection class
        results: list[Tuple[str: Any]] = connectToMySQL(db=cls.db).query_db(
            query=query, data=user_id)

        # Extract the user_data Dict from the results list
        user_data: Dict[str, Any] = results[0]

        try:
            # Try to instantiate the user and return the instance
            user: Self = cls(user_data)
            return user
        except Exception as e:
            # Print the exception of a user instance couldn't be created and return nothing
            print(f"Failed to create user: {e}")
            return False

    # Create Method, Union type hinting means that it can be one of multiple possible types, but only those included
    # In the list

    @classmethod
    def create_user(cls, user_data) -> Union[NoReturn, Literal[False]]:
        """
        Queries the 'users' table in the database to create a row with the
        user input data

        Args: 
            cls: The User Class
            user_data: An dictionary holding all the user input data

        Returns:
            None | Literal[False]: Returns nothing if successful, or False and prints the error if it failed
        """

        # Set query to insert row into users table in the database
        query = '''
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
                '''

        # Call connection method and query the database to create user and store result as a variable
        result: Union[NoReturn, Literal[False]] = connectToMySQL(
            db=cls.db).query_db(query=query, data=user_data)

        return result
