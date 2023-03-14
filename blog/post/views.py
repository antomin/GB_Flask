from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.models.post import Post
from blog.models.user import User

post = Blueprint('post', __name__, url_prefix='/posts', static_folder='../static')


@post.route('/')
def post_list():
    posts = Post.query.all()
    users = User.query.all()
    return render_template('post/list.html', users=users, posts=posts)


@post.route('/<int:pk>')
@login_required
def past_detail(pk: int):
    post = Post.query.filter_by(id=pk).one_or_none()
    user = User.query.filter_by(id=post.author).one_or_none()

    if not post:
        return NotFound('Статья не найденa.')

    return render_template('post/detail.html', user=user, post=post)