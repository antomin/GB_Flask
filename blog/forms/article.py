from flask_wtf import FlaskForm
from wtforms import (SelectMultipleField, StringField, SubmitField,
                     TextAreaField, validators)


class CreateArticleForm(FlaskForm):
    title = StringField('Название', validators=[validators.DataRequired()])
    text = TextAreaField('Текст', validators=[validators.DataRequired()])
    tags = SelectMultipleField('Теги', coerce=int)
    submit = SubmitField('Опубликовать')
