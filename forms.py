from flask_wtf import FlaskForm
from wtforms import (StringField)
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),
                                             Length(max=30)])
    password = StringField("Password", validators=[InputRequired(),
                                                   Length(max=30)])