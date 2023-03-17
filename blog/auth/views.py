from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extensions import db
from blog.forms import RegisterForm
from blog.forms.auth import LoginForm
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
    if current_user.is_authenticated:
        return redirect('main.index')

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))

        form.submit.errors.append('Неверный логин или пароль.')
        return render_template('auth/login.html', form=form)

    return render_template('auth/login.html', form=form)


@auth.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/registration', methods=['GET', 'POST'], endpoint='registration')
def register():
    if current_user.is_authenticated:
        return redirect('main.index')

    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('Пользователь с таким email уже существует!')
            return render_template('auth/registration.html', form=form)

        new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                        password=generate_password_hash(form.password.data))

        db.session.add(new_user)

        try:
            db.session.commit()
        except IntegrityError:
            form.submit.errors.append('Ошибка добавления пользователя.')
            return render_template('auth/registration.html', form=form)
        else:
            login_user(new_user)
            return redirect(url_for('main.index'))

    return render_template('auth/registration.html', form=form)
