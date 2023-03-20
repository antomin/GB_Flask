from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms import CreateArticleForm
from blog.models import Article, Author

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/')
def article_list():
    articles = Article.query.all()
    return render_template('article/list.html', articles=articles)


@article.route('/<int:pk>')
def get_article(pk: int):
    _article = Article.query.filter_by(id=pk).one_or_none()

    if not _article:
        return NotFound('Автор не найден.')

    return render_template('article/detail.html', article=_article)


@login_required
@article.route('/create', methods=['GET', 'POST'], endpoint='create')
def create_article():
    if not current_user.author:
        return redirect('author.create')

    form = CreateArticleForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        new_article = Article(title=form.title.data, text=form.text.data, author_id=current_user.author.id)

        db.session.add(new_article)

        try:
            db.session.commit()
        except IntegrityError as error:
            form.submit.errors.append(error)
            return render_template('article/create.html', form=form)
        else:
            return redirect(url_for('article.article_list'))

    return render_template('article/create.html', form=form)
