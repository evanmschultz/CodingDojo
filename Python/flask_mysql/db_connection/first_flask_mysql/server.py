from flask import Flask, redirect, render_template, request
# import the class from friend.py
from friend import Friend

app = Flask(import_name=__name__)


# Index Route
@app.route(rule="/", methods=["GET"])
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(f"\n{'_'*80}\n\n{friends}\n{'_'*80}\n")
    return render_template(template_name_or_list="index.jinja2", all_friends=friends)


# Create Friend Route
@app.route(rule='/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = request.form

    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data=data)
    # Don't forget to redirect after saving to the database.
    return redirect(location='/')


# Show Friend Route
@app.route(rule="/show_friend/<int:friend_id>", methods=['GET'])
def show_friend(friend_id):
    friend = Friend.get_friend_by_id(friend_id)

    return render_template(template_name_or_list="show_friend.jinja2", friend=friend, editing=False)


# Edit Friend View Route
@app.route(rule="/edit_friend/<int:friend_id>", methods=['GET'])
def edit_friend(friend_id):
    friend = Friend.get_friend_by_id(id=friend_id)

    return render_template(template_name_or_list="show_friend.jinja2", friend=friend, editing=True)


# Edit Friend POST Route
@app.route(rule='/update_friend/', methods=['POST'])
def update_friend():
    data = request.form
    Friend.update_friend(data=data)

    return redirect(location='/')


# Delete Friend POST Route
@app.route(rule="/delete_friend/<int:friend_id>", methods=['POST'])
def delete_friend(friend_id):
    Friend.delete_friend(friend_id=friend_id)

    return redirect(location="/")


if __name__ == "__main__":
    app.run(debug=True)
