# A cursor is the object we use to interact with the database
import pymysql.cursors


# This class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # Change the user and password as needed
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='rootroot',
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor,
                                     autocommit=False)
        # Establish the connection to the database
        self.connection = connection

    # The method to query the database

    def query_db(self, query: str, data: dict = None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query=query, args=data)
                print(f"\n{'_'*80}\n\nRunning Query: {query}\n{'_'*80}\n")

                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    row_id = cursor.lastrowid
                    print(f"\n\n{'_'*80}\nRow ID: {row_id}\n{'_'*80}\n")
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # If the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # Close the connection
                self.connection.close()


# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
