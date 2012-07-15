from django.contrib import admin
from repos.models import Repository


class RepositoryAdmin(admin.ModelAdmin):
    model = Repository

admin.site.register(Repository, RepositoryAdmin)
