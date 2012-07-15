from django.conf.urls import patterns, url
from repos import views as repo_views

urlpatterns = patterns('',
    url(r'^$', repo_views.HomeView.as_view(), name='home'),
    url(r'^profile/$', repo_views.ProfileView.as_view(), name='profile'),
)
