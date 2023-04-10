from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.extensions import db
from blog.models import User
from blog.permissions import UserPermission
from blog.schemas import UserSchema


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_get': [UserPermission]
    }
