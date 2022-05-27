from django.db import models


class BaseModel(models.Model):

    class ActiveObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(deleted_at=None)

    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ActiveObjects()
    all_objects = models.Manager()

    class Meta:
        abstract = True
