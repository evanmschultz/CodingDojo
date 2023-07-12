from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # Root route
def index():
    return render_template('main.jinja2')


@app.route('/play')  # route to play with defaults
@app.route('/play/<int:num>')  # set num and use the default color
@app.route('/play/<int:num>/<string:color>')  # set both color and num
def playground(num=3, color='#333'):
    return render_template('main.jinja2', num=num, color=color)


@app.errorhandler(404)  # Return 404 error for any routes not defined above
def not_found(event):
    return f'{event}'


if __name__ == "__main__":
    app.run(debug=True)
