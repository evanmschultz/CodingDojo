from flask_app.config.mySQLConnection import connectToMySQL
from flask_app.models.author import Author
from flask_app.models.book import Book

# Type hinting imports
from typing import Dict, List, Optional, Tuple
from pprint import pprint


class Favorite:
    database: str = 'books'

    @classmethod
    def add_favorite(cls, data: Dict) -> int:
        """
        Creates a favorite in the database.

        Args:
            data (Dict[str, int]): Favorite data. 
                {'book_id': int, 'author_id': int}

        Returns:
            int: The favorite's id, 0 if there is an Exception

        Raises:
            Exception: All exceptions raised during the execution of the query are re-raised.

        Notes:
            Calls the favorite_exists method to make sure the favorite doesn't already exist
            to prevent trying to pass in duplicates.  If a duplicate does exist, then 0 is
            returned.
        """

        query: str = """
                    INSERT INTO favorites (book_id, author_id)
                    VALUES (%(book_id)s, %(author_id)s);
        """
        results = 0

        if not cls.favorite_exists(data):
            results: int = connectToMySQL(
                cls.database).query_db(query, data)  # type: ignore

        return results

    @classmethod
    def get_favorites(cls, favorite_type: str, id: int) -> Tuple:
        """
        Fetch favorite books or authors for a given id.

        This function takes a user id and a favorite_type as inputs,
        then queries the database for the favorite books or authors
        associated with that user id. The favorite_type must be either 'book' or 'author'.

        Args:
            id (int): The id of the user.
            favorite_type (str): The type of favorite to fetch ('book' or 'author').

        Returns:
            Tuple: A tuple of dictionaries representing the favorite books or authors. 
            Empty Tuple: If no favorites are found, returns an empty tuple.

        Raises:
            ValueError: favorite_type must be 'book' or 'author'.
            Exception: All other exceptions raised during the execution of the query are re-raised.
        """
        if favorite_type not in ['book', 'author']:
            raise ValueError("favorite_type must be 'book' or 'author'")

        query: str = '''
                    SELECT * FROM books.authors
                    LEFT JOIN favorites ON favorites.author_id = authors.id
                    LEFT JOIN books ON favorites.book_id = books.id
        '''

        if favorite_type == 'book':
            query += '''WHERE books.id = %(id)s;'''
        else:
            query += '''WHERE authors.id = %(id)s;'''

        data: Dict = {'id': id}
        results: Optional[Tuple[dict]] = connectToMySQL(
            cls.database).query_db(query, data)  # type: ignore

        favorites: Tuple = ()
        if results:
            favorites = results
            pprint(favorites, indent=4)

        return favorites

    @classmethod
    def favorite_exists(cls, data: Dict) -> bool:
        """
        Checks if a favorite already exists in the database.

        Args:
            data (Dict[str, int]): Favorite data. 
                {'book_id': int, 'author_id': int}

        Returns:
            bool: True if the favorite exists, False otherwise
        """
        query: str = """
                    SELECT * FROM favorites 
                    WHERE book_id = %(book_id)s AND author_id = %(author_id)s;
        """
        result: Optional[Dict] = connectToMySQL(
            cls.database).query_db(query, data)  # type: ignore

        return bool(result)
