from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField


class Sumform(FlaskForm):
    num1 = IntegerField("number1")
    num2 = IntegerField("number2")
    submit = SubmitField("calculate Sum")


class Mulform(FlaskForm):
    num1 = IntegerField("number1")
    num2 = IntegerField("number2")
    submit = SubmitField("calculate Multiply")


class Divform(FlaskForm):
    num1 = IntegerField("number1")
    num2 = IntegerField("number2")
    submit = SubmitField("calculate Division")


class Subform(FlaskForm):
    num1 = IntegerField("number1")
    num2 = IntegerField("number2")
    submit = SubmitField("calculate Subtraction")


class Aveform(FlaskForm):
    num1 = IntegerField("number1")
    num2 = IntegerField("number2")
    submit = SubmitField("calculate Average")


class Percentform(FlaskForm):
    full_marks = IntegerField("enter the full marks")
    num1 = IntegerField("Bengali")
    num2 = IntegerField("English")
    num3 = IntegerField("Math")
    num4 = IntegerField("Science")
    num5 = IntegerField("History")
    num6 = IntegerField("Geography")
    submit = SubmitField("calculate percentage")


class Kathaform(FlaskForm):
    katha = IntegerField("Katha")
    submit = SubmitField("calculate square_feet")


class Bighaform(FlaskForm):
    bigha = IntegerField("bigha")
    submit = SubmitField("calculate square_feet")

class Kathabigform(FlaskForm):
    bigha = IntegerField("bigha")
    submit = SubmitField("calculate katha")

class Hectorform(FlaskForm):
    hector = IntegerField("hector")
    submit = SubmitField("calculate bigha")

class Kathahecform(FlaskForm):
    hector = IntegerField("hector")
    submit = SubmitField("calculate katha")
class Squarehecform(FlaskForm):
    hector = IntegerField("hector")
    submit = SubmitField("calculate square_feet")
