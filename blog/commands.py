from flask import Flask
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.models import User


def register_commands(app: Flask) -> None:
    @app.cli.command('create_admin')
    def create_admin():
        _email = input('Введите email администратора: ')
        _password = input('Введите пароль: ')
        _password_confirm = input('Повторите пароль: ')

        if _password != _password_confirm:
            print('Пароли не совпадают. Запустите команду заново.')
            return

        try:
            db.session.add(
                User(email='admin@admin.ru', is_staff=True, password=generate_password_hash('admin'), first_name='Admin')
            )

            db.session.commit()

        except Exception as er:
            print(er)
            return

        print(f'Администратор создан!')

    app.cli.add_command(create_admin)
