from django.conf.urls import url
from .views import *

app_name = "work"

urlpatterns = [

    url(r'^$', work_view, name="index"),
    url(r'^add/$', add_view, name="add"),

]