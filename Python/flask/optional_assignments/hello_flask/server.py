# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/success')
def success():
    return 'Success'  # Return the string 'Success' as a response


@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    # Return name passed in as variable after hello in the browser
    return f'Hello {name * num}'


@app.route('/lists')
def render_lists():
    # Dictionary to be rendered in a table using Jinja
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    # Pass in a list and the dictionary to the template
    return render_template("lists.html", random_numbers=[3, 1, 5], students=student_info)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
