from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators


class CreateArticleForm(FlaskForm):
    title = StringField('Название', validators=[validators.DataRequired()])
    text = TextAreaField('Текст', validators=[validators.DataRequired()])
    submit = SubmitField('Опубликовать')
