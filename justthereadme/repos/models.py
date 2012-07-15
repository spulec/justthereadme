from django.db import models

from repos.managers import RepositoryManager


class Repository(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    readme_text = models.TextField()

    objects = RepositoryManager()

    class Meta:
        unique_together = ('user', 'name')

    def __unicode__(self):
        return u"Repo: {}-{}".format(self.user, self.name)
