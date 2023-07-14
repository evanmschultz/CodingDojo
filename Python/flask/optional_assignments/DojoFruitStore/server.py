from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    form_data = {}
    # Loop over request.form and add inform each key: value pair to form_data
    for key, value in request.form.items():
        form_data[key] = value

    print(
        f'Charging {form_data["first_name"]} {form_data["last_name"]} for {form_data["strawberry"] + form_data["raspberry"] + form_data["apple"]} fruits')

    # Pass these variables to render_template
    return render_template("checkout.html", form_data=form_data)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
