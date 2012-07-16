from django.conf.urls import patterns, url
from repos import views as repo_views

urlpatterns = patterns('',
    url(r'^$', repo_views.HomeView.as_view(), name='home'),
    url(r'^about/$', repo_views.AboutView.as_view(), name='about'),
    url(r'^profile/$', repo_views.ProfileView.as_view(), name='profile'),
    url(r'^repo/(?P<repo_id>\d+)/activate$', repo_views.ActivateRepoView.as_view(activate=True), name='activate_repo'),
    url(r'^repo/(?P<repo_id>\d+)/deactivate$', repo_views.ActivateRepoView.as_view(activate=False), name='deactivate_repo'),
    url(r'^repo/(?P<repo_id>\d+)/update$', repo_views.UpdateRepoView.as_view(), name='update_repo'),
)
