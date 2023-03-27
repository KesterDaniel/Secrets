from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, EmailField)
from wtforms.validators import InputRequired, Length, Email


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(max=8)])
    submit = SubmitField("Submit")
