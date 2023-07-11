from flask import Flask, render_template

# Instantiate a flask instance called app
app = Flask(__name__)


@app.route('/')  # Root route
def index():
    return render_template('index.jinja2')


@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<string:color>')
def playground(num=3, color='#333'):
    return render_template('play.jinja2', num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
