from datetime import datetime
from typing import Dict, List, Optional, Tuple

from flask_app.config.mySQLConnection import connectToMySQL


class Favorite:
    database: str = 'books'

    def __init__(self, data: Dict) -> None:
        """Instantiates a Favorite instance"""
        self.book_id: int = data['book_id']
        self.author_id: int = data['author_id']
        self.created_at: datetime = data['created_at']
        self.updated_at: datetime = data['updated_at']

    @classmethod
    def add_favorite(cls, data: Dict) -> int:
        """
        Creates a favorite in the database.

        Args:
            Dict[str, int]: Favorite data. 
                {'book_id': int, 'author_id': int}

        Returns:
            int: The favorite's id, 0 if there is an Exception

        Raises:
            TypeError: book_id and author_id must be ints.
            Exception: All other exceptions raised during the execution of the query are re-raised.

        Notes:
            Returns 0 or index for extensibility. A boolean locks this method into simple functionality.
            If for whatever reason the id of the favorite instance is important in the future it will be
            available without refactoring.
        """
        if not isinstance(data['book_id'], int) or not isinstance(data['author_id'], int):
            print(
                f"\n\n{'_'*80}\n\nTypeError:\n\nbook_id and author_id must be ints!\n{'_'*80}")
            return 0

        query: str = """
                    INSERT INTO favorites (book_id, author_id)
                    VALUES (%(book_id)s, %(author_id)s);
        """
        try:
            favorite_id: int = connectToMySQL(
                cls.database).query_db(query, data)  # type: ignore
            return favorite_id
        except Exception as e:
            print(
                f"\n\n{'_'*80}\n\nError ocurred while creating favorite:\n\n{e}\n{'_'*80}")
            return 0

    @classmethod
    def get_favorites(cls, favorite_type: str, id: int) -> List['Favorite']:
        """
        Gets favorite's data from the database.

        Args:
            favorite_type: str - The type of favorite ('book' or 'author')
            id: int - The id of the favorite type

        Returns:
            List[Author] or List[Book]: List of instances of the Favorite class associated with a book or an author.
            Empty List: If there are no favorites in the database or an exception is raised.

        Raises:
            ValueError: favorite_type must be 'book' or 'author'.
            Exception: All other exceptions raised during the execution of the query are re-raised.
        """
        if favorite_type not in ['book', 'author']:
            raise ValueError("favorite_type must be 'book' or 'author'")

        query: str = '''SELECT * FROM favorites '''

        if favorite_type == 'book':
            query += '''WHERE book_id = %(id)s;'''
        else:
            query += '''WHERE author_id = %(id)s;'''

        data: Dict = {'id': id}
        results: Optional[Tuple[dict]] = connectToMySQL(
            cls.database).query_db(query, data)  # type: ignore

        favorites = []
        try:
            if results:
                favorites: List[Favorite] = [
                    cls(favorite) for favorite in results]
        except Exception as e:
            print(
                f"\n\n{'_'*80}\n\nError occurred while instantiating Favorite(s):\n\n{e}\n{'_'*80}")

        return favorites
