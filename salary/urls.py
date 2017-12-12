from django.conf.urls import url
from .views import *

app_name = "salary"

urlpatterns = [

    url(r'^$', salary_view, name="index"),
    url(r'^add/$', add_view, name="add"),

]