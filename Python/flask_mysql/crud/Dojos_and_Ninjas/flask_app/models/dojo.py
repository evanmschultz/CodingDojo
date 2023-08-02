from flask_app.config.mysql_connection import connectToMySQL
from datetime import datetime
from typing import Self


class Dojo:
    database: str = 'dojos_and_ninjas'

    def __init__(self, data: dict) -> None:
        """Instantiates a Dojo instance"""
        self.id: int = data['id']
        self.name: str = data['name']
        self.created_at: datetime = data['created_at']
        self.updated_at: datetime = data['updated_at']

    @classmethod
    def get_dojos(cls) -> list:
        """
        Gets every dojo's data from the database.

        Returns:
            list: A list of the Dojos class instances, or empty list if there are no dojos
            in the database or an exception is raised.

        Raises:
            Any exception is handled by the query_db method from connectToMySQL().
        """
        query: str = 'SELECT * FROM dojos;'
        results: tuple[dict[str, int | str | datetime]] | None = connectToMySQL(
            cls.database).query_db(query)  # type: ignore

        print(results)
        dojos = []
        if results:
            dojos: list[Self] = [cls(dojo) for dojo in results]

        return dojos

    @classmethod
    def create_dojo(cls, dojo_data: dict) -> int:
        """
        Creates a dojo in the database from user input.

        Args:
            dojo_data (dict): dict[str, int | str].

        Returns:
            int: The dojo's id.

        Raises:
            Any exception is handled by the query_db method from connectToMySQL().
        """
        query: str = """
                    INSERT INTO dojos (name)
                    VALUES %(name)s;
        """

        dojo_id: int = connectToMySQL(cls.database).query_db(
            query, dojo_data)  # type: ignore

        return dojo_id
