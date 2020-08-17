from django.db import models
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeleteManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        return SoftDeleteQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()

    def get_default(self, **kwargs):
        return self.get_queryset().filter(is_deleted=False, **kwargs)


class SoftDeleteQuerySet(models.query.QuerySet):
    def delete(self):
        return super(SoftDeleteQuerySet, self).update(
            deleted_at=timezone.now(), is_deleted=True
        )

    def restore(self):
        return super(SoftDeleteQuerySet, self).update(
            deleted_at=None, is_deleted=False
        )

    def hard_delete(self):
        return super(SoftDeleteQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)
