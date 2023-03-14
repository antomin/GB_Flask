from flask import Flask

from blog.auth.view import auth, login_manager
from blog.commands import register_commands
from blog.config import DevConfig
from blog.main.view import main
from blog.models.database import db
from blog.post.views import post
from blog.user.views import user


def create_app() -> Flask:
    app = Flask(__name__)
    register_commands(app)
    app.config.from_object(DevConfig)
    db.init_app(app)
    register_blueprints(app)
    login_manager.init_app(app)
    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(auth)
    app.register_blueprint(main)
