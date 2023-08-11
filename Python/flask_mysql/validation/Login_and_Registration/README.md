# Login and Registration - Flask Application

## Description

This is a Flask web application created for a [Coding Dojo](https://www.codingdojo.com) assignment. The application provides a platform for user login and registration, featuring authentication and validation mechanisms. It demonstrates skills in user authentication, validation, session management, and uses bcrypt for password hashing and Pydantic for data validation.

## Features

-   **User Registration**: Allows new users to create an account with validation checks.
-   **User Login**: Existing users can log in with their email and password.
-   **Dashboard Access**: Authenticated users are redirected to a dashboard.
-   **Password Security**: Passwords are securely hashed using bcrypt.
-   **Input Validation**: Utilizes Pydantic to validate user input during registration.
-   **Session Management**: Utilizes sessions to store and confirm user IDs.
-   **Simple, Clean Design**: The pages are designed to simple and clean using the Skeleton CSS framework.

## Database

This application uses MySQL for database management. The database schema is available in the MWB file included in the repository. Ensure that MySQL is installed and properly configured on your system.

### Importing the Database

1. Open MySQL Workbench.
2. Navigate to 'File' > 'Open Model' and select the MWB file.
3. Forward Engineer the model to create the database.

## License

MIT License.

This project is simply a [Coding Dojo](https://www.codingdojo.com) assignment.

## Author

Evan Schultz
