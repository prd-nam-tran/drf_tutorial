from django.conf import settings
from django.db import models


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now_add=True, editable=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, null=True,
                                   db_column="created_by", related_name="%(class)s_create_by",
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, null=True,
                                   db_column="updated_by", related_name="%(class)s_update_by",
                                   on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['-id']
