import uuid

from django.db import models

from model_utils.models import TimeStampedModel
from django.utils.text import slugify


class Club(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    def save(self,
             force_insert=False,
             force_update=False,
             using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        if update_fields is not None and "name" in update_fields:
            update_fields = {"slug"}.union(update_fields)
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
