from flask_app.config.mySQLConnection import connectToMySQL
from flask_app.models import book

# Type hinting imports
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class Author:
    database: str = 'books'

    def __init__(self, data: Dict) -> None:
        """Instantiates a Author instance"""
        self.id: int = data['id']
        self.name: str = data['name']
        self.created_at: datetime = data['created_at']
        self.updated_at: datetime = data['updated_at']

    @classmethod
    # Quotes around author is Forward Referencing the class for type hinting
    def get_authors(cls, get_single: Optional[bool] = False, author_id: Optional[int] = None) -> List['Author']:
        """
        Gets author's data from the database.

        If get_single is set to True, method will return a list with a single author from 
        the database. Otherwise it will return a list of every author from the database.

        Args:
            bool: Optional get_single boolean
            int: Optional author_id int

        Returns:
            List[Author]: List of instances of the Author class.
            Empty List: If there are no authors in the database or an exception is raised.

        Raises:
            Exception: Class instantiation error.
            Exception: All other exceptions raised during the execution of the query are re-raised.

        Notes:
            If get_single is set to True and no author_id is passed in as an argument an error will
            print in the console and an empty list will be returned.
        """
        data: Dict = {}
        if not get_single:
            query: str = '''SELECT * FROM authors;'''
        else:
            if not author_id:
                print(
                    f"\n\n{'_'*80}\n\nAn author_id must be passed in as an argument if get_single is True.\n{'_'*80}")
                return []

            query: str = '''
                        SELECT * FROM authors
                        WHERE id = %(id)s
            '''
            data = {'id': author_id}

        results: Optional[Tuple[dict]] = connectToMySQL(
            cls.database).query_db(query, data)  # type: ignore

        authors = []
        try:
            if results:
                authors: List[Author] = [cls(author) for author in results]
        except Exception as e:
            print(
                f"\n\n{'_'*80}\n\nError ocurred while instantiating Author(s):\n\n{e}\n{'_'*80}")

        return authors

    @classmethod
    def create_author(cls, author_data: Dict) -> int:
        """
        Creates a author in the database from user input.

        Args:
            Dict[str, str]: Book data. {'name': str}

        Returns:
            int: The author's id.

        Raises:
            TypeError: Name must be a str.
            Exception: All other exceptions raised during the execution of the query are re-raised.
        """
        query: str = '''
                    INSERT INTO authors (name)
                    VALUES (%(name)s);
        '''

        if not isinstance(author_data['name'], str):
            print(
                f"\n\n{'_'*80}\n\nTypeError:\n\nname must be a str!\n{'_'*80}")
            return 0

        author_id: int = connectToMySQL(
            cls.database).query_db(query, author_data)  # type: ignore

        return author_id
