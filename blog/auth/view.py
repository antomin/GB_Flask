from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

from blog.models import User

auth = Blueprint('auth', __name__, static_folder='static')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def get_user(pk: int) -> User:
    user = User.query.filter_by(id=pk).one_or_none()
    return user


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')

    email = request.form.get('login')
    password = request.form.get('password')

    if not email:
        return render_template('auth/login.html', error='Email или пароль не введены. Попробуйте снова.')

    user = User.query.filter_by(email=email).one_or_none()

    if not user:
        return render_template('auth/login.html', error='Пользователь не найден. Попробуйте снова.')

    login_user(user)
    return redirect(url_for('main.index'))


@auth.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
