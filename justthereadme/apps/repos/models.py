from docutils.core import publish_parts
from docutils.writers.html4css1 import Writer

SETTINGS = {
    'cloak_email_addresses': True,
    'file_insertion_enabled': False,
    'raw_enabled': False,
    'strip_comments': True,
    'doctitle_xform': False,
    'report_level': 5,
}

from django.db import models
from django.utils.safestring import mark_safe

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

    @property
    def formatted_html(self):
        return mark_safe(publish_parts(self.readme_text, writer=Writer(), settings_overrides=SETTINGS)['html_body'])
