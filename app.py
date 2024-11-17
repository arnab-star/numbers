from flask import Flask, render_template

from form import Divform, Subform, Sumform, Mulform

app = Flask(__name__)

app.secret_key = "hello india"


@app.get("/")
def hello_world():
    return "<h1>hello_Arnab</h3>"


@app.get("/upper/<name>")
def convert_to_upper(name):
    upper_name = name.upper
    return upper_name


@app.get("/sum/<a>/<b>")
def sum_int(a, b):
    sum = int(a) + int(b)
    return f"<h1 style ='font-size :100px'>{sum}</h1>"


@app.get("/temperature/<c>")
def convert_to_f(c):
    convert = float(9 / 5) * int(c) + 32
    return f"{convert}"


@app.route("/sum", methods=['Get', 'Post'])
def sum():
    form = Sumform()
    total = None
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        total = num1 + num2
    return render_template('sum.html', form=form, total=total)


@app.route("/mul", methods=['Get', 'Post'])
def multiply():
    form = Mulform()
    total = None
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        total = num1 + num2
    return render_template('multiply.html', form=form, total=total)


@app.route("/division", methods=['Get','Post'])
def divison():
    form = Divform()
    total = None
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        total = num1 / num2
    return render_template('division.html', form=form, total=total)


@app.route("/subtraction", methods=['Get','Post'])
def subtraction():
    form = Subform()
    total = None
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        total = num1 - num2
    return render_template('subtraction.html', form=form, total=total)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5052,debug=True)
