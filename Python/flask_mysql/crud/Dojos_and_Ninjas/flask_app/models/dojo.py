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

            # Sorts using an anonymous function, sorting by name
            dojos = sorted(dojos, key=lambda dojo: dojo.name)

        return dojos

    @classmethod
    def get_dojo(cls, dojo_id: int) -> Self | None:
        query: str = """
                    SELECT * FROM dojos
                    WHERE id = %(id)s;
        """

        id: dict = {'id': dojo_id}
        results: tuple[dict] = connectToMySQL(
            cls.database).query_db(query, id)  # type: ignore

        if results:
            dojo_data: dict = results[0]
        else:
            print(
                f"\n\n{'_'*80}No results were found with id = {dojo_id} or the query failed.\n{'_'*80}")
            return None

        try:
            dojo: Self = cls(dojo_data)
            return dojo
        except Exception as e:
            print(
                f"\n\n{'_'*80}Failed to create ninja, exception:\n\n{e}\n{'_'*80}")
            return None

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
                    VALUES (%(name)s);
        """

        dojo_id: int = connectToMySQL(cls.database).query_db(
            query, dojo_data)  # type: ignore

        return dojo_id

    @classmethod
    def update_dojo(cls, dojo_data: dict) -> int:
        """
        Updates a dojo in the database from user input.

        Args:
            dojo_data (dict): dict[str, int | str].

        Returns:
            int: The dojo's id.

        Raises:
            Any exception is handled by the query_db method from connectToMySQL().
        """
        query: str = """
                    UPDATE dojos
                    SET name = %(name)s
                    WHERE id = %(id)s;
        """
        print(dojo_data)
        connectToMySQL(cls.database).query_db(query, dojo_data)
        dojo_id: int = dojo_data['id']

        return dojo_id

    @classmethod
    def delete_dojo(cls, dojo_id: int) -> None:
        """
        Deletes a dojo from the database using the dojo's id.

        Args:
            dojo_id (int): The dojo's id.

        Returns:
            None: Nothing is returned

        Raises:
            Any exception is handled by the query_db method from connectToMySQL().
        """
        query: str = """
                    DELETE FROM dojos
                    WHERE id = %(id)s;
        """

        data: dict = {'id': dojo_id}
        connectToMySQL(cls.database).query_db(
            query, data)  # type: ignore

        return None
