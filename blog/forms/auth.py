from flask_wtf import FlaskForm
from wtforms import (EmailField, PasswordField, StringField, SubmitField,
                     validators)


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Пароль', validators=[validators.DataRequired()])
    submit = SubmitField('Вход')


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[validators.DataRequired(), validators.Email()])
    first_name = StringField('Имя')
    last_name = StringField('Фамилия')
    password = PasswordField('Пароль', validators=[
        validators.DataRequired(), validators.EqualTo('password_confirm', message='Пароли не совпадают')])
    password_confirm = PasswordField('Повторите пароль', validators=[validators.DataRequired()])
    submit = SubmitField('Регистрация')


