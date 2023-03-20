from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms import RegisterAuthorForm
from blog.models import Article, Author

author = Blueprint('author', __name__, url_prefix='/authors', static_folder='../static')


@author.route('/')
def author_list():
    authors = Author.query.all()
    return render_template('author/list.html', authors=authors)


@author.route('/<int:pk>')
def get_author(pk: int):
    _author = Author.query.filter_by(id=pk).one_or_none()
    articles = Article.query.filter_by(author_id=_author.id)

    if not _author:
        return NotFound('Автор не найден.')

    return render_template('author/detail.html', author=_author, articles=articles)


@login_required
@author.route('/create', methods=['GET', 'POST'], endpoint='create')
def create_author():
    if current_user.author:
        return redirect('main.index')

    form = RegisterAuthorForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        new_author = Author(user_id=current_user.id)

        db.session.add(new_author)
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data

        try:
            db.session.commit()
        except IntegrityError as error:
            form.submit.errors.append(error)
            return render_template('author/create.html', form=form)
        else:
            return redirect(url_for('main.index'))

    return render_template('author/create.html', form=form)
