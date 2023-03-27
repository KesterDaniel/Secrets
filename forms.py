from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired(), Length(max=30)])
    submit = SubmitField("Submit")
