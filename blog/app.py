from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from combojsonapi.spec import ApiSpecPlugin
from flask import Flask

from blog.admin import admin
from blog.api import (ArticleDetail, ArticleList, AuthorDetail, AuthorList,
                      TagDetail, TagList, UserDetail, UserList)
from blog.article.views import article_app
from blog.auth.views import auth_app, login_manager
from blog.author.views import author_app
from blog.commands import register_commands
from blog.config import DevConfig, BaseConfig
from blog.extensions import api, db, migrate
from blog.main.view import main_app
from blog.user.views import user_app


def create_app() -> Flask:
    app = Flask(__name__)
    register_commands(app)
    app.config.from_object(BaseConfig)
    register_extensions(app)
    register_blueprints(app)
    register_api(app)
    return app


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)
    admin.init_app(app)


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(user_app)
    app.register_blueprint(author_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(main_app)
    app.register_blueprint(article_app)


def register_api(app: Flask) -> None:
    api.plugins = [
        # EventPlugin(),
        PermissionPlugin(strict=False),
        ApiSpecPlugin(
            app=app,
            tags={
                'Tag': 'Tags API',
                'Article': 'Article API',
                'Author': 'Author API',
                'User': 'User API'
            }
        ),

    ]

    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>/', tag='Tag')
    api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>/', tag='Article')
    api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>/', tag='Author')
    api.route(UserList, 'user_list', '/api/users/', tag='User')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>/', tag='User')

    api.init_app(app)
