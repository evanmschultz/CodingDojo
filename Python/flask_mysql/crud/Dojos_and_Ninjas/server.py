from flask_app import app
# TODO import controllers
from flask_app.controllers import dojos, ninjas

if __name__ == "__main__":
    app.run(debug=True)
