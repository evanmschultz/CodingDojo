import pymysql.cursors
from flask_app.config.mysql_connection import connectToMySQL
from datetime import datetime


class MySQLConnection:
    def __init__(self, db: str) -> None:
        """Instantiates a connection instance"""
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

    def query_db(self, query: str, data: dict[str, str | int] = {}) -> int | tuple[dict[str, str | int | datetime]] | None:
        """
        Executes a SQL query on the database (SELECT, INSERT, UPDATE, DELETE).

        This method commits the query and closes the connection after execution, regardless of success or failure.

        Args:
            query (str): The SQL query to be executed.
            data (dict[str, str | int], optional): The data to be used in the query, if any. Defaults to an empty dict.

        Returns:
            tuple[dict[str, str | int | datetime], ...]: SELECT queries, returns the fetched data as a tuple of dictionaries.
            int: INSERT queries, returns the row ID of the inserted row.
            None: UPDATE and DELETE queries, return nothing

        Raises:
            Exception: Any exceptions raised during the execution of the query are re-raised.
        """
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print(f'\n{"_"*80}\n\nRunning Query: {query}\n{"_"*80}\n')

                cursor.execute(query)

                # SELECT query
                if query.lower().find('select'):
                    self.connection.commit()

                    results: tuple[dict[str, str | int |
                                        datetime], ...] = cursor.fetchall()
                    return results
                # INSERT query
                elif query.lower().find('insert'):
                    self.connection.commit()
                    row_id: int = cursor.lastrowid
                    return row_id
                # UPDATE and DELETE queries (nothing is returned)
                else:
                    self.connection.commit()

            except Exception as e:
                print(
                    f'\n{"_"*80}\n\nSomething went wrong: {e}\n{"_"*80}\n')
                raise

            finally:
                # Close the connection
                self.connection.close()


def connectToMySQL(db: str) -> MySQLConnection:
    """
    Instantiates an instance of the MySQLConnection class to create a connection to the database argument.

    Args:
        db (str): A string of the name of the database to create a connection with

    Returns:
        MySQLConnection(db): An instance of the connection
    """
    return MySQLConnection(db)
