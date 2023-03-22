from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import User

user_app = Blueprint('user_app', __name__, url_prefix='/users', static_folder='../static')


@user_app.route('/')
def user_list():
    users = User.query.all()
    return render_template('user/list.html', users=users)


@user_app.route('/<int:pk>')
def get_user(pk: int):
    user = User.query.filter_by(id=pk).one_or_none()

    if not user:
        return NotFound('Пользователь не найден.')

    return render_template('user/detail.html', user=user)
