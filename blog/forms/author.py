from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class RegisterAuthorForm(FlaskForm):
    first_name = StringField('Имя', validators=[validators.DataRequired()])
    last_name = StringField('Фамилия', validators=[validators.DataRequired()])
    submit = SubmitField('Стать автором')
