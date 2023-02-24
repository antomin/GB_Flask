from flask import Flask

from blog.post.views import post
from blog.user.views import user


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(user)
    app.register_blueprint(post)
