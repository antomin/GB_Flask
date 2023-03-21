from flask import Flask
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.models import Tag, User


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
                User(email=_email, is_staff=True, password=generate_password_hash(_password), first_name='Admin')
            )

            db.session.commit()

        except Exception as er:
            print(er)
            return

        print(f'Администратор создан!')

    @app.cli.command('create_tags')
    def create_tags():
        for item in ("flask", "django", "python", "sqlalchemy","news",):
            tag = Tag(name=item)
            db.session.add(tag)
        db.session.commit()
        print('Done!')

    app.cli.add_command(create_tags)
    app.cli.add_command(create_admin)
