from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.forms import RegisterForm
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


@auth.route('/registration', methods=['GET', 'POST'], endpoint='registration')
def register():
    if current_user.is_authenticated:
        return redirect('main.index')

    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('Пользователь с таким email уже существует!')
            return render_template('auth/registration.html', form=form)

        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )

        db.session.add(new_user)

        try:
            db.session.commit()
        except IntegrityError:
            form.submit.errors.append('Ошибка добавления пользователя.')
        else:
            login_user(new_user)
            return redirect(url_for('main.index'))

    return render_template('auth/registration.html', form=form)
