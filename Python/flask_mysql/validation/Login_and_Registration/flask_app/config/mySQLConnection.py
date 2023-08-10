import pymysql.cursors

# Type hinting imports
from typing import Dict, Optional, Tuple, Any
from datetime import datetime


class MySQLConnection:
    def __init__(self, db: str) -> None:
        """Instantiates a connection instance.

        Args:
            db (str): Database name for the connection.
        """
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='rootroot',
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False
        )
        # Establish the connection to the database
        self.connection = connection

    def _execute_query(self, query: str, query_type: str, data: Dict[str, str | int] = {}) -> Any:
        """Execute a SQL query on the database.

        Args:
            query (str): The SQL query to be executed.
            query_type (str): The type of query (SELECT, UPDATE, DELETE, or INSERT).
            data (Dict[str, str | int], optional): The data to be used in the query. Defaults to an empty dict.

        Returns:
            cursor (Any): The cursor object after executing the query.

        Raises: 
            Exception: Any exceptions raised during the execution of the query are caught and printed, but not re-raised.
        """
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print(f'\n{"_"*80}\n\nRunning Query: {query}\n{"_"*80}\n')
                cursor.execute(query)
                return cursor
            except Exception as e:
                print(
                    f'\n{"_"*80}\n\nDatabase {query_type} error:\n\n{e}\n{"_"*80}\n')
                raise

    def close_connection(self) -> None:
        """Closes the connection to the database."""
        self.connection.close()

    def select_from_db(self, query: str, data: Dict = {}) -> Tuple[Dict]:
        """Execute a SQL SELECT query on the database.

        Args:
            query (str): The SQL query to be executed.
            data (Dict[str, str | int], optional): The data to be used in the query. Defaults to an empty dict.

        Returns:
            results (Tuple): Returns the fetched data as a tuple.

        Raises:
            Exception: Exception: All exceptions are raised by the _execute_query method and printed.
        """
        cursor = self._execute_query(query, 'SELECT', data)
        self.connection.commit()
        results = cursor.fetchall()

        # Close connection
        self.close_connection()
        return results

    def insert_into_db(self, query: str, data: Dict) -> int:
        """Execute a SQL INSERT query on the database.

        Args:
            query (str): The SQL query to be executed.
            data (Dict[str, str | int]): The data to be used in the query.

        Returns:
            row_id (int): Returns the row ID of the inserted row.
        """
        cursor = self._execute_query(query, 'INSERT', data)
        self.connection.commit()
        row_id: int = cursor.lastrowid

        # Close connection
        self.close_connection()
        return row_id

    def update_db(self, query: str, data: Dict) -> int:
        """Execute a SQL UPDATE query on the database.

        Args:
            query (str): The SQL query to be executed.
            data (Dict[str, str | int]): The data to be used in the query.

        Returns: 
            row_id (int): The ID of the updated row.
        """
        row_id: Optional[int] = data.get('id')
        if not row_id:
            row_id = 0
            raise ValueError("Missing 'id' key in data")
        self._execute_query(query, 'UPDATE', data)
        self.connection.commit()

        # Close connection
        self.close_connection()
        return row_id

    def delete_from_db(self, query: str, data: Dict) -> None:
        """Execute a SQL DELETE query on the database.

        Args:
            query (str): The SQL query to be executed.
            data (Dict[str, str | int]): The data to be used in the query.

        Returns:
            None
        """
        self._execute_query(query, 'DELETE', data)
        self.connection.commit()

        # Close connection
        self.close_connection()


def connectToMySQL(db: str) -> MySQLConnection:
    """Instantiates an instance of the MySQLConnection class to create a connection to the database.

    Args:
        db (str): A string of the name of the database to create a connection with.

    Returns:
        MySQLConnection: An instance of the connection.
    """
    return MySQLConnection(db)
