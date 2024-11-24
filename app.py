from flask import Flask, render_template

from form import Divform, Subform, Aveform, Mulform, Sumform, Percentform, Kathaform

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


@app.route("/division", methods=['Get', 'Post'])
def division():
    form = Divform()
    total = None
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        total = num1 / num2
    return render_template('division.html', form=form, total=total)


@app.route("/subtraction", methods=['Get', 'Post'])
def subtraction():
    form = Subform()
    total = None
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        total = num1 - num2
    return render_template('subtraction.html', form=form, total=total)


@app.route("/average", methods=['Get', 'Post'])
def average():
    form = Aveform()
    total = None
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        total = num1 + num2
        average = total / 2
    return render_template('average.html', form=form, average=average)


@app.route("/percentage", methods=['Get', 'Post'])
def percentage():
    form = Percentform()
    percentage = None
    if form.validate_on_submit():
        full_marks = form.full_marks.data
        num1 = form.num1.data
        num2 = form.num2.data
        num3 = form.num3.data
        num4 = form.num4.data
        num5 = form.num5.data
        num6 = form.num6.data
        total = num1 + num2 + num3 + num4 + num5 + num6
        percentage = (total / (6*full_marks)) *100
    return render_template('percentage.html', form=form, percentage=percentage)

@app.route("/katha", methods=['Get', 'Post'])
def katha():
    form = Kathaform()
    square_feet = None
    if form.validate_on_submit():
        num1 = form.katha.data
        square_feet = num1 * 720
    return render_template('katha.html', form = form, square_feet=square_feet)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5052, debug=True)
