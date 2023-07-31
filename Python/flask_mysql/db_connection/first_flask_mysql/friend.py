# Import the function that will return an instance of a connection
from unittest import result
from mysql_connection import connectToMySQL


# Model the class after the friend table from our database
class Friend:
    database = 'flask_friends'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # READ Methods
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"

        # Make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(db='flask_friends').query_db(query=query)

        # Create a user instance and add it to the list
        friends = [cls(friend) for friend in results]
        return friends

    @classmethod
    def get_friend_by_id(cls, id):
        query = """
                SELECT * FROM friends
                WHERE id = %(id)s
                """

        data = {"id": id}
        results = connectToMySQL(db=cls.database).query_db(
            query=query, data=data)
        friend = results[0]

        return cls(friend)

    # CREATE Method
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO friends (first_name, last_name, occupation) 
                VALUES (%(first_name)s, %(last_name)s, %(occupation)s);
                """

        # The data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(db=cls.database).query_db(
            query=query, data=data)

        return result

    # UPDATE Method
    @classmethod
    def update_friend(cls, data):
        query = '''
                UPDATE friends
                SET first_name = %(first_name)s, last_name = %(last_name)s, occupation = %(occupation)s
                WHERE id = %(id)s;
                '''

        results = connectToMySQL(db=cls.database).query_db(
            query=query, data=data)

        return results

    # DELETE Method

    @classmethod
    def delete_friend(cls, friend_id):
        query = '''
                DELETE FROM friends
                WHERE id = %(id)s;
                '''

        data = {'id': friend_id}
        results = connectToMySQL(db=cls.database).query_db(
            query=query, data=data)

        return results
