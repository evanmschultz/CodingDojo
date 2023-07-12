from flask import Flask, render_template

# instantiate flask instance named app
app = Flask(__name__)


@app.route('/')  # Default checkerboard
@app.route('/<int:x_total>')  # Set num of (x_total)
@app.route('/<int:x_total>/<int:y_total>')  # Set num of (y_total)
# Set the first color
@app.route('/<int:x_total>/<int:y_total>/<string:color_1>')
@app.route('/<int:x_total>/<int:y_total>/<string:color_1>/<string:color_2>')
# Set the second color
def checkerboard(x_total=8, y_total=8, color_1='#222222', color_2='#dedede'):
    return render_template('main.jinja2', x_total=x_total, y_total=y_total, color_1=color_1, color_2=color_2)


@app.errorhandler(404)  # Return 404 error for any routes not defined above
def not_found(event):
    return f'{event}'


if __name__ == "__main__":
    app.run(debug=True)
