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
