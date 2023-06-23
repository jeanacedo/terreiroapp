from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email

class FormLogin(FlaskForm):
    username = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar acesso')
    button_submit = SubmitField('Login')