import base64
from celery.decorators import task
from github import Github
import requests

from django.contrib.auth.models import User


@task
def update_user_repos(user_id):
    from repos.models import Repository

    user = User.objects.get(id=user_id)
    github_user = user.social_auth.get(provider='github')
    access_token = github_user.extra_data.get('access_token')
    if not access_token:
        return
    github = Github(access_token)
    for repo in github.get_user().get_repos():
        new_repo, created = Repository.objects.get_or_create(user=user, name=repo.name, defaults={
            'url': repo.html_url,
            'readme_text': '',
        })
        if created:
            update_repository(new_repo.id)


@task
def update_repository(repository_id):
    from repos.models import Repository

    repository = Repository.objects.get(id=repository_id)
    base_url = u"https://api.github.com/repos/{user}/{repo_name}/readme"
    url = base_url.format(user=repository.user.username, repo_name=repository.name)
    response = requests.get(url, timeout=20)
    if response.ok:
        readme_content = base64.decodestring(response.json['content'])
        if repository.readme_text != readme_content:
            repository.readme_text = readme_content
            repository.save()
