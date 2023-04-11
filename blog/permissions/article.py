from combojsonapi.permission import (PermissionForGet, PermissionMixin,
                                     PermissionUser)
from combojsonapi.permission.permission_system import PermissionForPatch
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from blog.models import Article


class ArticlePermissions(PermissionMixin):
    PATCH_AVAILABLE_FIELDS = ['title', 'text']

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(self, *args, data=None, obj=None, user_permission: PermissionUser = None, **kwargs) -> dict:
        if current_user.id != obj.author_id or not current_user.is_staff:
            raise AccessDenied('You don`t have access!')

        permission_for_patch = user_permission.permission_for_patch_permission(model=Article)
        return {key: value for key, value in data.items() if key in self.PATCH_AVAILABLE_FIELDS}
