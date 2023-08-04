from flask_app.config.mysql_connection import connectToMySQL
from datetime import datetime
from typing import Self


class Ninja:
    database: str = 'dojos_and_ninjas'

    def __init__(self, data: dict) -> None:
        """Instantiates a Ninja instance"""
        self.id: int = data['id']
        self.first_name: str = data['first_name']
        self.last_name: str = data['last_name']
        self.age: int = data['age']
        self.dojo_id: int = data['dojo_id']
        self.created_at: datetime = data['created_at']
        self.updated_at: datetime = data['updated_at']

    @classmethod
    def get_ninjas(cls, dojos_id: int) -> list:
        """
        Gets every ninja's data from the database.

        Returns:
            list: A list of the Ninja class instances, or an empty list if there are no ninjas
            in the database or an exception is raised.

        Raises:
            Any exception is handled by the query_db method from connectToMySQL().
        """
        query: str = '''
                    SELECT * FROM ninjas
                    WHERE %(dojos_id)s = dojo_id;
        '''

        data: dict = {'dojos_id': dojos_id}
        results: tuple[dict] | None = connectToMySQL(
            cls.database).query_db(query, data)  # type: ignore

        print(results)
        ninjas = []
        if results:
            ninjas: list[Self] = [cls(ninja) for ninja in results]

        return ninjas

    @classmethod
    def get_ninja(cls, ninja_id: int) -> Self | None:
        """
        Gets the ninja data from the database using the ninja's id.

        Args:
            ninja_id (int): The ninja's id.

        Returns:
            Self: An instance of the Ninja class.

        Raises:
            Prints 'Failed to create user, exception: {exception}' to the console.
        """
        query: str = """
                    SELECT * FROM ninjas
                    WHERE id = %(id)s;
        """

        id: dict = {'id': ninja_id}
        results: tuple[dict] = connectToMySQL(
            cls.database).query_db(query, id)  # type: ignore

        if results:
            ninja_data: dict = results[0]
        else:
            print(
                f"\n\n{'_'*80}No results were found with id = {ninja_id} or the query failed.\n{'_'*80}")
            return None

        try:
            ninja: Self = cls(ninja_data)
            return ninja
        except Exception as e:
            print(
                f"\n\n{'_'*80}Failed to create ninja, exception:\n\n{e}\n{'_'*80}")
            return None

    @classmethod
    def create_ninja(cls, ninja_data: dict) -> int:
        """
        Creates a ninja in the database from user input.

        Args:
            ninja_data (dict): dict[str, int | str].

        Returns:
            int: The ninja's id.

        Raises:
            Any exception is handled by the query_db method from connectToMySQL().
        """

        query: str = """
                    INSERT INTO ninjas (first_name, last_name, age, dojo_id)
                    VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """

        ninja_id: int = connectToMySQL(
            cls.database).query_db(query, ninja_data)  # type: ignore

        return ninja_id

    @classmethod
    def update_ninja(cls, ninja_data: dict) -> None:
        """
        Updates a ninja in the database with the user input data.

        Args:
            ninja_data (dict): A dictionary (dict[str, int | str]).
             (): .

        Returns:
            None: Nothing is returned.

        Raises:
            Any exception is handled by the query_db method from connectToMySQL().
        """

        query: str = """
                    UPDATE ninjas
                    SET first_name = %(first_name)s, last_name = %(last_name)s, 
                    age = %(age)s, dojo_id = %(dojo_id)s
                    WHERE id = %(id)s;
        """

        connectToMySQL(cls.database).query_db(
            query, ninja_data)  # type: ignore

        return None

    @classmethod
    def delete_ninja(cls, ninja_id: int) -> None:
        """
        Deletes a ninja from the database using the ninja's id.

        Args:
            ninja_id (int): The ninja's id.

        Returns:
            None: Nothing is returned

        Raises:
            Any exception is handled by the query_db method from connectToMySQL().
        """

        query: str = """
                    DELETE FROM ninjas
                    WHERE id = %(id)s;
        """

        data: dict = {'id': ninja_id}
        connectToMySQL(cls.database).query_db(
            query, data)  # type: ignore

        return None
