from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms import CreateArticleForm
from blog.models import Article, Tag

article_app = Blueprint('article_app', __name__, url_prefix='/articles', static_folder='../static')


@article_app.route('/')
def article_list():
    articles = Article.query.all()
    return render_template('article/list.html', articles=articles)


@article_app.route('/<int:pk>')
def get_article(pk: int):
    _article = Article.query.filter_by(id=pk).options(joinedload(Article.tags)).one_or_none()

    if not _article:
        return NotFound('Автор не найден.')

    return render_template('article/detail.html', article=_article)


@login_required
@article_app.route('/create', methods=['GET', 'POST'], endpoint='create')
def create_article():
    if not current_user.author:
        return redirect(url_for('author_app.create'))

    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if request.method == 'POST' and form.validate_on_submit():
        new_article = Article(title=form.title.data, text=form.text.data, author_id=current_user.author.id)

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                new_article.tags.append(tag)

        db.session.add(new_article)

        try:
            db.session.commit()
        except IntegrityError as error:
            form.submit.errors.append(error)
            return render_template('article/create.html', form=form)
        else:
            return redirect(url_for('article_app.article_list'))

    return render_template('article/create.html', form=form)
