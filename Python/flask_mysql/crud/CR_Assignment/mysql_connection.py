# A cursor is the object we use to interact with the database and has built in methods
from pymysql import Connection
import pymysql.cursors
# Type hinting imports
from typing import Any, Dict, Literal, Optional, Tuple


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

    def query_db(self, query: str, data: Optional[Dict[str, Any]] = None) -> int | Tuple[Dict[str, Any], ...] | Literal[False] | None:
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

                    result: Tuple[Dict[str, Any]] = cursor.fetchall()
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


def connectToMySQL(db) -> MySQLConnection:
    """
    Instantiates an instance of the MySQLConnection class to create a connection to the database argument

    Args:
        db: A string of the name of the database to create a connection with

    Returns:
        MySQLConnection(db): An instance of the connection
    """
    return MySQLConnection(db=db)
