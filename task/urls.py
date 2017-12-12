from django.conf.urls import url
from .views import *

app_name = "task"

urlpatterns = [

    url(r'^$', task_view, name="index"),
    url(r'^add/$', create_view, name="add"),
    url(r'^confirm/$', confirm_task_view, name="confirm"),
    url(r'^(?P<t_slug>[\w-]+)/work/$', task_work, name="work"),
    url(r'^(?P<t_slug>[\w-]+)/fault/$', task_fault, name="fault"),
    url(r'^(?P<t_slug>[\w-]+)/$', detail_view, name="detail"),
    url(r'^(?P<t_slug>[\w-]+)/update/$', update_view, name="update"),

]