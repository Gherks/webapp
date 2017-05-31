from flask_wtf import FlaskForm
from wtforms import StringField, validators


class MyForm(FlaskForm):
    first_name = StringField('First name', [validators.InputRequired()])
    last_name = StringField('Last name', [validators.InputRequired()])
    miscellaneous = StringField('Miscellaneous', [validators.InputRequired()])
