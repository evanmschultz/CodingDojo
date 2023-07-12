from flask import Flask

# Create a flask instance called app
app = Flask(__name__)


@app.route('/')  # Render Hello World in the root route
def hello_world():
    return 'Hello World!'


@app.route('/dojo')  # Render Dojo
def dojo():
    return 'Dojo!'


@app.route('/say/<name>')  # Render Hi {name}
def say_hi(name):
    return f'Hi {name}!'


@app.route('/repeat/<int:num>/<string:word>')  # Repeat word num times
def repeat(num, word):
    return f'{word * num}'


@app.errorhandler(404)  # Return 404 error for any routes not defined above
def not_found(event):
    return f'{event}'


if __name__ == "__main__":
    app.run(debug=True)
