# A cursor is the object we use to interact with the database and has built in methods
import pymysql.cursors
# Type hinting imports
from typing import Any, Literal


class MySQLConnection:
    def __init__(self, db) -> None:
        """
        Instantiates connection to MySQL database.

        Args:
            self: The connection.
            db: A string of the database name

        Returns:
            list[Self]: A list of User instances populated with data from 
            the database.
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

    def query_db(self, query: str, data: dict[str, Any] = {}) -> int | tuple[dict[str, Any]] | Literal[False] | None:
        """
        Executes a SQL query on the database. Depending on the type of query, different results are returned.

        This method commits the query and closes the connection after execution, regardless of success or failure.

        Args:
            query (str): The SQL query to be executed.
            data (dict[str, Any], optional): The data to be used in the query, if any. Defaults to None.

        Returns:
            int: If an INSERT query was executed, the method returns the row ID of the inserted row.
            Tuple[dict[str, Any], ...]: If a SELECT query was executed, the method returns the fetched data as a tuple of dictionaries.
            Literal[False]: If the query execution fails, the method returns False.
            None: If an UPDATE or DELETE query was executed, the method returns None as these queries don't have a return value.

        Raises:
            Exception: Any exceptions raised during the execution of the query are caught and printed, but not re-raised.

        Note:
            This method assumes a connection is already established, and will close the connection after execution.
        """
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query=query, args=data)
                print(f'\n{"_"*80}\n\nRunning Query: {query}\n{"_"*80}\n')

                cursor.execute(query=query)

                # The find method returns the lowest index of the the substring, thus it returns -1 if the substring
                # is not found in the string. Therefore, 0 could mean that the substring was found.
                if query.lower().find('insert') >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    row_id: int = cursor.lastrowid

                    print(f"\n\n{'_'*80}\nRow ID: {row_id}\n{'_'*80}\n")
                    return row_id

                elif query.lower().find('select') >= 0:
                    # SELECT queries will return the data from the database as a TUPLE OF DICTIONARIES using pymysql
                    self.connection.commit()

                    result: tuple[dict[str, Any]] = cursor.fetchall()
                    return result

                else:
                    # UPDATE or DELETE will return nothing
                    self.connection.commit()

            except Exception as exception:
                # If the query fails the method will return FALSE
                print(
                    f'\n{"_"*80}\n\nSomething went wrong: {exception}\n{"_"*80}\n')
                return False

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
    return MySQLConnection(db=db)
