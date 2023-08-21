from pydantic import BaseModel, Field
from datetime import date


class TV_ShowData(BaseModel):
    """
    A Pydantic BaseModel class for TV show data validation.

    Pydantic's Field and validator methods are used to enforce these rules.

    The following fields are used to validate the TV show's information:
    1. `title`: Ensures the title is at least 3 characters long.
    2. `description`: Ensures the description is at least 3 characters long.
    3. `network`: Ensures the network is at least 3 characters long.
    4. `release_date`: Ensures the date is in the correct format (yyyy-mm-dd).

    If any of the validations fail, a ValueError is thrown.
    """

    title: str = Field(
        ...,
        min_length=3,
        description="Ensures the title is at least 3 characters long.",
    )
    description: str = Field(
        ...,
        min_length=3,
        description="Ensures the description is at least 3 characters long.",
    )
    network: str = Field(
        ...,
        min_length=3,
        description="Ensures the network is at least 3 characters long.",
    )
    release_date: date = Field(
        ..., description="Ensures the date is in the correct format (yyyy-mm-dd)."
    )

    class Config:
        """
        Configuration class for additional schema settings.

        It includes json_schema_extra for providing an example that can be used for documentation or testing.
        """

        json_schema_extra = {
            "example": {
                "title": "Futurama",
                "description": """
                                An animated series that follows the adventures of a late-20th-century New York 
                                City pizza delivery boy, Philip J. Fry, who, after being unwittingly cryogenically 
                                frozen for one thousand years, finds employment at Planet Express, an interplanetary 
                                delivery company in the retro-futuristic 31st century.
                """,
                "network": "FOX",
                "release_date": "1999-03-28",
            }
        }


from pydantic import ValidationError


def main():
    # Test Case 1: Valid TV Show Data
    valid_show_data: dict = {}
    try:
        valid_show_data = {
            "title": "Breaking Bad",
            "description": "A high school chemistry teacher turned methamphetamine producer.",
            "network": "AMC",
            "release_date": date(2008, 1, 20),
        }
        tv_show = TV_ShowData(**valid_show_data)
        print("Valid TV Show:", tv_show)
    except ValidationError as e:
        print("Validation Error for Valid TV Show:", e)

    # Test Case 2: Invalid Title (less than 3 characters)
    try:
        invalid_title_data = valid_show_data.copy()
        invalid_title_data["title"] = "BB"
        tv_show = TV_ShowData(**invalid_title_data)
    except ValidationError as e:
        print("Validation Error for Invalid Title:", e)

    # Test Case 3: Invalid Release Date Format
    try:
        invalid_date_data = valid_show_data.copy()
        invalid_date_data["release_date"] = "20-01-2008"
        tv_show = TV_ShowData(**invalid_date_data)
    except ValidationError as e:
        print("Validation Error for Invalid Release Date Format:", e)


if __name__ == "__main__":
    main()
