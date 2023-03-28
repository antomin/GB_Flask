from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.extensions import db
from blog.models import Article, Author
from blog.schemas import AuthorSchema


class AuthorDetailEvent(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {
            'count': Article.query.filter(Article.author_id == kwargs.get('id')).count()
        }


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author
    }


class AuthorDetail(ResourceDetail):
    events = AuthorDetailEvent
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author
    }
