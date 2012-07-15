from django.db.models import Manager
from django.db.models.query import QuerySet


class RepositoryQueryset(QuerySet):
    def active(self):
        return self.filter(active=True)


class RepositoryManager(Manager):
    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)

    def get_query_set(self):
        return RepositoryQueryset(self.model)
