from flask import Flask
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.models import User


def register_commands(app: Flask) -> None:
    @app.cli.command('create_admin')
    def create_admin():
        db.session.add(
            User(email='admin@admin.ru', is_staff=True, password=generate_password_hash('admin'), first_name='Admin')
        )

        db.session.commit()

        print('Admin user with default params added!')

    app.cli.add_command(create_admin)
