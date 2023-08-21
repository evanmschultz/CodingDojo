from typing import Optional
from flask import flash
from pydantic import ValidationError
from flask_app.config.mySQLConnection import connectToMySQL
from flask_app.models.tv_show_model.tv_show_validation import TV_ShowData

# Type hinting import
from datetime import datetime, date


class TV_Show:
    """The TV_Show class"""

    database: str = "tv_shows"

    def __init__(self, data: dict) -> None:
        """Instantiates a TV_Show instance"""
        self.id: int = data["id"]
        self.title: str = data["title"]
        self.network: str = data["network"]
        self.release_date: date = data["release_date"]
        self.description: str = data["description"]
        self.user_id: int = data["user_id"]
        self.creator_first_name: Optional[str] = None
        self.creator_last_name: Optional[str] = None
        self.created_at: datetime = data["created_at"]
        self.updated_at: datetime = data["updated_at"]

        # Will be calculated in get_all... and get_tv_show_by_id methods
        self.likes_count: int = 0
        self.like_user_ids: list[int] = data.get("like_user_ids", [])

    @classmethod
    def get_all_tv_shows(cls) -> list["TV_Show"]:
        """
        Gets all the tv_shows from the database.

        Returns:
            list: A list of instances of the tv_show class.
        """
        query: str = """
                    SELECT tv_shows.id AS id,
                        tv_shows.user_id AS user_id,
                        tv_shows.title,
                        tv_shows.network,
                        tv_shows.release_date,
                        tv_shows.description,
                        tv_shows.created_at,
                        tv_shows.updated_at,
                        likes.user_id AS like_user_id
                    FROM tv_shows
                    LEFT JOIN likes ON tv_shows.id = likes.tv_show_id;
        """
        results: tuple[dict] = connectToMySQL(cls.database).select_from_db(query)

        grouped_results: dict = {}
        for result in results:
            tv_show_id: int = result["id"]
            if tv_show_id not in grouped_results:
                grouped_results[tv_show_id] = {
                    "id": result["id"],
                    "user_id": result["user_id"],
                    "title": result["title"],
                    "network": result["network"],
                    "release_date": result["release_date"],
                    "description": result["description"],
                    "created_at": result["created_at"],
                    "updated_at": result["updated_at"],
                    "like_user_ids": [],
                    "likes_count": 0,
                }
            if result["like_user_id"] is not None:
                grouped_results[tv_show_id]["like_user_ids"].append(
                    result["like_user_id"]
                )
                grouped_results[tv_show_id]["likes_count"] += 1

        tv_shows: list[TV_Show] = [
            cls(tv_show_data) for tv_show_data in grouped_results.values()
        ]

        return tv_shows

    @classmethod
    def get_tv_show_by_id(cls, tv_show_id: int) -> Optional["TV_Show"]:
        """
        Gets a single tv_show from the database by its ID, including the name from the row in the
        users table where the users.id matches the user_id.

        Args:
            tv_show_id (int): The ID of the tv_show to retrieve.

        Returns:
            TV_Show: An instance of the TV_Show class, or None if not found.
        """
        query: str = """
                    SELECT tv_shows.*, users.first_name AS creator_first_name, users.last_name AS creator_last_name, likes.user_id AS like_user_id
                    FROM tv_shows
                    LEFT JOIN users ON tv_shows.user_id = users.id
                    LEFT JOIN likes ON tv_shows.id = likes.tv_show_id
                    WHERE tv_shows.id = %(id)s;
        """
        data: dict = {"id": tv_show_id}
        results: tuple[dict] = connectToMySQL(cls.database).select_from_db(query, data)

        tv_show: Optional[TV_Show] = None
        if results:
            tv_show = cls(results[0])
            tv_show.creator_first_name = results[0]["creator_first_name"]
            tv_show.creator_last_name = results[0]["creator_last_name"]

            for result in results:
                if result["like_user_id"] is not None:
                    tv_show.like_user_ids.append(result["like_user_id"])
                    tv_show.likes_count += 1

        return tv_show

    @classmethod
    def add_tv_show(cls, tv_show_data: dict) -> int:
        """
        Adds a tv_show to the database.

        Args:
            tv_show_data (dict): The tv_show data, including:
                {
                    'title': str,
                    'network': str,
                    'release_date': date,
                    'description': str,
                    'user_id': int
                }

        Returns:
            int: The ID of the created tv_show.
        """
        query: str = """
                    INSERT INTO tv_shows (title,  network, release_date, description, user_id)
                    VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s);
        """

        tv_show_id: int = connectToMySQL(cls.database).insert_into_db(
            query, tv_show_data
        )
        return tv_show_id

    @classmethod
    def update_tv_show(cls, tv_show_data: dict) -> int:
        """
        Updates the tv_show in the database

        Args:
            tv_show_data (dict): A dictionary holding all the updated data.
                {
                    'id': int
                    'title': str,
                    'network': str,
                    'release_date': date,
                    'description': str,
                }

        Returns:
            int: Returns the row_id of the updated tv_show.
        """
        query: str = """
                    UPDATE tv_shows
                    SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s
                    WHERE id = %(id)s;
        """

        tv_show_id: int = connectToMySQL(db=cls.database).update_db(
            query=query, data=tv_show_data
        )

        return tv_show_id

    @classmethod
    def delete_tv_show(cls, tv_show_id: int) -> None:
        """
        Deletes the tv_show from the database.

        Args:
            tv_show_id (int): The id of the tv_show to delete from the database.
        """
        query: str = """
                    DELETE FROM tv_shows
                    WHERE id = %(id)s;
        """
        data: dict = {"id": tv_show_id}

        connectToMySQL(db=cls.database).delete_from_db(query=query, data=data)

    @staticmethod
    def like_tv_show(user_id: int, tv_show_id: int) -> None:
        """
        Adds a like to a specific TV show by a user.

        Args:
            user_id (int): The ID of the user liking the TV show.
            tv_show_id (int): The ID of the TV show being liked.
        """
        query: str = """
                    INSERT INTO likes (user_id, tv_show_id)
                    VALUES (%(user_id)s, %(tv_show_id)s);
        """
        data: dict = {"user_id": user_id, "tv_show_id": tv_show_id}
        connectToMySQL(TV_Show.database).insert_into_db(query, data)

    @staticmethod
    def unlike_tv_show(user_id: int, tv_show_id: int) -> None:
        """
        Removes a like from a specific TV show by a user.

        Args:
            user_id (int): The ID of the user unliking the TV show.
            tv_show_id (int): The ID of the TV show being unliked.
        """
        query: str = """
                    DELETE FROM likes
                    WHERE user_id = %(user_id)s AND tv_show_id = %(tv_show_id)s;
        """
        data: dict = {"user_id": user_id, "tv_show_id": tv_show_id}
        connectToMySQL(TV_Show.database).delete_from_db(query, data)

    @staticmethod
    def validate_tv_show(tv_show_data: dict) -> bool:
        """
        Validates TV show inputs using the Pydantic schema in the TV_ShowData class.

        Args:
            tv_show_data (dict): The TV show data from the input form, including:
                {
                    'title': str,         # At least 3 characters long
                    'description': str,   # At least 3 characters long
                    'network': str,       # At least 3 characters long
                    'release_date': str   # Correct format (yyyy-mm-dd)
                }

        Returns:
            boolean: True if validation checks pass, False otherwise.
        """
        try:
            TV_ShowData(**tv_show_data)
            return True
        except ValidationError as e:
            for error in e.errors():
                field_name = str(error["loc"][0])
                error_type = error["type"]

                if error_type == "string_too_short":
                    flash(
                        f"{field_name.capitalize()} needs to be at least 3 characters long.",
                        "tv_show_error",
                    )
                elif error_type == "date_from_datetime_parsing":
                    flash("Release Date is required.", "tv_show_error")

            return False
