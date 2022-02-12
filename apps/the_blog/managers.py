from django.db import models
from django.db.models import Q

class PostQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query=='':
            return self.none()
        lookups = Q(title__icontains=query) | Q(body__icontains=query)
        return self.filter(lookups)



class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)