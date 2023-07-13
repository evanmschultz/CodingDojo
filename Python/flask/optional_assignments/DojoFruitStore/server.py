from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    # Get quantities of each fruit from request.form
    strawberry_count = int(request.form.get('strawberry', 0))
    raspberry_count = int(request.form.get('raspberry', 0))
    apple_count = int(request.form.get('apple', 0))

    # Get customer's information from request.form
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    student_id = request.form.get('student_id', '')

    print(
        f'Charging {first_name} {last_name} for {strawberry_count + raspberry_count + apple_count} fruits')

    # Pass these variables to render_template
    return render_template("checkout.html", strawberry_count=strawberry_count,
                           raspberry_count=raspberry_count, apple_count=apple_count,
                           first_name=first_name, last_name=last_name, student_id=student_id)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
