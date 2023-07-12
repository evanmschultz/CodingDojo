from flask import Flask, render_template

# Instantiate Flask instance named app
app = Flask(__name__)


@app.route('/')
def index():
    # Dictionary of users to be rendered on index template
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]

    # Render template and pass users as an argument
    return render_template('index.jinja2', users=users)


if __name__ == "__main__":
    app.run(debug=True)
