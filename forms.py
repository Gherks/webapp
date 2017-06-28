from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class ContactForm(FlaskForm):
    first_name = StringField('First name', [validators.InputRequired()])
    last_name = StringField('Last name', [validators.InputRequired()])
    miscellaneous = StringField('Miscellaneous', [validators.InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])
