from pydantic import BaseModel, field_validator
from datetime import datetime


class RecipeData(BaseModel):
    """
    A Pydantic BaseModel class for recipe data validation.

    Pydantic's field_validator methods are used to enforce these rules.

    The following class methods are used to validate the recipe's information:
    1. `validate_name`: Ensures the name is at least 3 characters long.
    2. `validate_description`: Ensures the description is at least 10 characters long but less than 255.
    3. `validate_instructions`: Ensures the instructions are at least 20 characters long but less than 1000.
    4. `validate_date_made`: Ensures the date is in the correct format (yyyy-mm-dd).
    5. `validate_under_30_min`: Ensures the value is either 0 (false) or 1 (true).

    If any of the validations fail, a ValueError is thrown.
    """

    name: str
    description: str
    instructions: str
    date_made: str
    under_30_min: int

    @field_validator("name")
    def validate_name(cls, value: str) -> str:
        """
        Ensures that the name is at least 3 characters long.

        Args:
            value (str): The name value.

        Returns:
            str: The validated name value.

        Raises:
            ValueError: If the name value is less than 3 characters.
        """
        if len(value.strip()) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        return value

    @field_validator("description")
    def validate_description(cls, value: str) -> str:
        """
        Ensures that the description is at least 10 characters long but less than 255.

        Args:
            value (str): The description value.

        Returns:
            str: The validated description value.

        Raises:
            ValueError: If the description value is not within the specified length range.
        """
        length = len(value.strip())
        if length < 10 or length > 255:
            raise ValueError(
                "Description must be at least 10 characters long and less than 255."
            )
        return value

    @field_validator("instructions")
    def validate_instructions(cls, value: str) -> str:
        """
        Ensures that the instructions are at least 20 characters long but less than 1000.

        Args:
            value (str): The instructions value.

        Returns:
            str: The validated instructions value.

        Raises:
            ValueError: If the instructions value is not within the specified length range.
        """
        length = len(value.strip())
        if length < 20 or length > 1000:
            raise ValueError(
                "Instructions must be at least 20 characters long and less than 1000."
            )
        return value

    @field_validator("date_made")
    def validate_date_made(cls, value: str) -> str:
        """
        Ensures that the date_made is in the correct format (yyyy-mm-dd).

        Args:
            value (str): The date_made value.

        Returns:
            str: The validated date_made value.

        Raises:
            ValueError: If the date_made value is not in the correct format.
        """
        try:
            datetime.strptime(value.strip(), "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in the format yyyy-mm-dd.")
        return value

    @field_validator("under_30_min")
    def validate_under_30_min(cls, value: int) -> int:
        """
        Ensures that the value is either 0 (false) or 1 (true).

        Args:
            value (int): The under_30_min value.

        Returns:
            int: The validated under_30_min value.

        Raises:
            ValueError: If the value is not 0 or 1.
        """
        if value not in (0, 1):
            raise ValueError("under_30_min must be 0 for false or 1 for true.")
        return value
