from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from repos.models import Repository
from repos.tasks import update_repository


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # TODO setup cache
        repos = Repository.objects.active()
        for repo in repos:
            repo.formatted_readme = repo.formatted_html
        context = {'repos': repos}
        return self.render_to_response(context)


class AboutView(TemplateView):
    template_name = 'about.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        repos = Repository.objects.filter(user=request.user)
        for repo in repos:
            repo.formatted_readme = repo.formatted_html
        context = {'repos': repos}
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)


class ActivateRepoView(TemplateView):
    activate = True

    def get(self, request, *args, **kwargs):
        return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        try:
            repo_id = int(kwargs.get('repo_id'))
        except ValueError:
            return HttpResponseForbidden()

        repo = get_object_or_404(Repository, id=repo_id)
        if request.user.id != repo.user_id:
            return HttpResponseForbidden()

        if repo.active != self.activate:
            repo.active = self.activate
            repo.save()
        return HttpResponse()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ActivateRepoView, self).dispatch(request, *args, **kwargs)


class UpdateRepoView(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        try:
            repo_id = int(kwargs.get('repo_id'))
        except ValueError:
            return HttpResponseForbidden()

        repo = get_object_or_404(Repository, id=repo_id)
        if request.user.id != repo.user_id:
            return HttpResponseForbidden()

        update_repository(repo.id)
        return HttpResponse()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateRepoView, self).dispatch(request, *args, **kwargs)
