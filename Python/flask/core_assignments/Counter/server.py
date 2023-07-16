from flask import Flask, render_template, redirect, session

app = Flask(__name__)
# Set secret key to access session, update using environment variable if deploying
app.secret_key = 'secret_key'


@app.route('/')
def index():
    # Increment visits value in session dictionary if reloaded
    session['visits'] = session.get('visits', 0) + 1
    print(session['visits'])
    return render_template('index.jinja2', visits=session['visits'])


@app.route('/increment', methods=['POST'])
def increment():
    # Increment visits value in session dictionary if reloaded
    session['visits'] = session.get('visits', 0) + 1
    print(session['visits'])
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
