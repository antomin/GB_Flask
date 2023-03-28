from combojsonapi.spec import ApiSpecPlugin
from flask import Flask
from flask_combo_jsonapi import Api

from blog.api.article import ArticleDetail, ArticleList
from blog.api.author import AuthorDetail, AuthorList
from blog.api.tag import TagDetail, TagList
from blog.api.user import UserDetail, UserList


def create_api_spec_plugin(app):
    return ApiSpecPlugin(
        app=app,
        tags={
            'Tag': 'Tags API',
            'Article': 'Article API',
            'Author': 'Author API',
            'User': 'User API'
        }
    )
#
#
# def init_api(app: Flask) -> None:
#     api = Api(
#         app=app,
#         plugins=[create_api_spec_plugin(app), ]
#     )
#
#     api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
#     api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>/', tag='Tag')
#     api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
#     api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>/', tag='Article')
#     api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
#     api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>/', tag='Author')
#     api.route(UserList, 'user_list', '/api/users/', tag='User')
#     api.route(UserDetail, 'user_detail', '/api/users/<int:id>/', tag='User')


__all__ = ['TagList', 'TagDetail', 'ArticleDetail', 'ArticleList', 'AuthorDetail', 'AuthorList',
           'UserDetail', 'UserList']
