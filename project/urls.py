from django.conf.urls import url
from .views import active_project_view, confirm_project_view, project_create, project_detail, project_update, project_vote, project_task

app_name = "project"
urlpatterns = [
    url(r'^$', active_project_view, name="index"),
    url(r'^create/$', project_create, name="create"),
    url(r'^confirm$', confirm_project_view, name="confirm"),
    url(r'^(?P<p_slug>[\w-]+)/vote/$', project_vote, name="vote"),
    url(r'^(?P<p_slug>[\w-]+)/$', project_detail, name="detail"),
    url(r'^(?P<p_slug>[\w-]+)/update/$', project_update, name="update"),
    url(r'^(?P<p_slug>[\w-]+)/task/$', project_task, name="task"),


]
