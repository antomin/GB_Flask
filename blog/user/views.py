from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {1: 'Alice', 2: 'Bob', 3: 'Charlie'}


@user.route('/')
def user_list():
    return render_template('user/list.html', users=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user = USERS[pk]
    except KeyError:
        return NotFound('Пользователь не найден.')
    return render_template('user/detail.html', user=user)
