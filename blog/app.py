from flask import Flask

from blog.article.views import article
from blog.auth.views import auth, login_manager
from blog.author.views import author
from blog.commands import register_commands
from blog.config import DevConfig
from blog.extensions import db, migrate
from blog.main.view import main
from blog.user.views import user


def create_app() -> Flask:
    app = Flask(__name__)
    register_commands(app)
    app.config.from_object(DevConfig)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(user)
    app.register_blueprint(author)
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(article)

