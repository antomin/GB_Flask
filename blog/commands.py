from flask import Flask

from blog.models import Post
from blog.models.database import db

LOREM_TEXT = 'Mauris ultrices vehicula nisl, ut finibus libero efficitur ac. Vivamus est nisi, condimentum nec tortor id, ' \
       'euismod interdum massa. Sed eros ex, rutrum eu tincidunt non, scelerisque at felis. Nam id nisi non lacus' \
       'faucibus pretium. Pellentesque fermentum magna eros, egestas molestie urna consequat tempor. Maecenas sagittis' \
       'vulputate pellentesque. Cras.'


def register_commands(app: Flask) -> None:
    @app.cli.command('init-db')
    def init_db():
        db.create_all()
        print('Done!')

    @app.cli.command('fill-db')
    def fill_db():
        from blog.models import User

        db.session.add_all([
            User(username='admin', email='admin@admin.ru', is_staff=True),
            User(username='alice', email='alice@admin.ru'),
            User(username='bob', email='bob@admin.ru'),
            User(username='charlie', email='charlie@admin.ru'),

            Post(title='Статья №1', text=LOREM_TEXT+'1', author=2),
            Post(title='Статья №2', text=LOREM_TEXT+'2', author=3),
            Post(title='Статья №3', text=LOREM_TEXT+'3', author=4),
        ])

        db.session.commit()

        print('Done!')

    app.cli.add_command(init_db)
    app.cli.add_command(fill_db)
