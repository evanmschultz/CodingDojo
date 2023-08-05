from flask_app.config.mySQLConnection import connectToMySQL

# Type hinting imports
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class Book:
    database: str = 'books'

    def __init__(self, data: dict) -> None:
        """Instantiates a Book instance"""
        self.id: int = data['id']
        self.title: str = data['title']
        self.num_of_pages: int = data['num_of_pages']
        self.favorites: List = []
        self.created_at: datetime = data['created_at']
        self.updated_at: datetime = data['updated_at']

    @classmethod
    # Quotes around book is Forward Referencing the class for type hinting
    def get_books(cls, get_single: Optional[bool] = False, book_id: Optional[int] = None) -> List['Book']:
        """
        Gets book's data from the database.

        If get_single is set to True, method will return a list with a single book from 
        the database. Otherwise it will return a list of every book from the database.

        Args:
            bool: Optional get_single boolean
            int: Optional book_id int

        Returns:
            List[Book]: List of instances of the Book class.
            Empty List: If there are no books in the database or an exception is raised.

        Raises:
            Exception: Any exceptions raised during the execution of the query are re-raised.

        Notes:
            If get_single is set to True and no book_id is passed in as an argument an error will
            print in the console and an empty list will be returned.
        """
        data: Dict = {}
        if not get_single:
            query: str = '''SELECT * FROM books;'''
        else:
            if not book_id:
                print(
                    f"\n\n{'_'*80}\n\nAn book_id must be passed in as an argument if get_single is True.\n{'_'*80}")
                return []

            query: str = '''
                        SELECT * FROM books
                        WHERE id = %(id)s;
            '''
            data = {'id': book_id}

        results: Optional[Tuple[dict]] = connectToMySQL(
            cls.database).query_db(query, data)  # type: ignore

        books = []
        try:
            if results:
                books: List[Book] = [cls(book) for book in results]
        except Exception as e:
            print(
                f"\n\n{'_'*80}\n\nError ocurred while instantiating Book(s):\n\n{e}\n{'_'*80}")

        return books

    @classmethod
    def create_book(cls, book_data: Dict) -> int:
        """
        Creates a book in the database from user input.

        Args:
            Dict[str, str, int]: Book data. 
                {'title': str, 'num_of_pages': int}

        Returns:
            int: The book's id.

        Raises:
            TypeError: Title must be a str and num_of_pages must be an int.
            Exception: All other exceptions raised during the execution of the query are re-raised.
        """
        query: str = '''
                    INSERT INTO books (title, num_of_pages)
                    VALUES (%(title)s, %(num_of_pages)s);
        '''

        if not isinstance(book_data['title'], str):
            print(
                f"\n\n{'_'*80}\n\nTypeError:\n\ntitle must be a str and num_of_pages must be an int!\n{'_'*80}")
            return 0

        book_id: int = connectToMySQL(
            cls.database).query_db(query, book_data)  # type: ignore

        return book_id
