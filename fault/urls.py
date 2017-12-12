from django.conf.urls import url
from .views import *

app_name = "fault"

urlpatterns = [

    url(r'^$', fault_view, name="index"),

    url(r'^add/$', add_view, name="add"),
    url(r'^(?P<f_slug>[\w-]+)/$', detail_view, name="detail"),
    url(r'^(?P<f_slug>[\w-]+)/update/$', update_view, name="update"),

]