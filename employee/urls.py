from django.conf.urls import url
from .views import *

app_name = "employee"

urlpatterns = [

    url(r'^$', employee_view, name="index"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^profile/$', profile_view, name="profile"),
    url(r'^(?P<e_slug>[\w-]+)/$', detail_view, name="detail"),
    url(r'^(?P<e_slug>[\w-]+)/update/$', update_profile_view, name="update"),

]
