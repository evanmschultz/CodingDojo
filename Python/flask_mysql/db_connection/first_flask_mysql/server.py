from flask import Flask, redirect, render_template, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(f"\n{'_'*80}\n\n{friends}\n{'_'*80}\n")
    return render_template("index.jinja2", all_friends=friends)


@app.route(("/show_friend/<int:friend_id>"))
def show_friend(friend_id):
    friend = Friend.get_friend_by_id(friend_id)

    return render_template("show_friend.jinja2", friend=friend)


@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = request.form

    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
