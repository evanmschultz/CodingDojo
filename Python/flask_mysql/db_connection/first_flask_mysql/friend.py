# import the function that will return an instance of a connection
from mysql_connection import connectToMySQL
# model the class after the friend table from our database


class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(db='flask_friends').query_db(query=query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append(cls(friend))
        return friends

    # class method to save our friend to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation) VALUES (%(first_name)s, %(last_name)s, %(occupation)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(db='flask_friends').query_db(query=query, data=data)
