from django.conf.urls import url
from . import views

app_name = 'certifs'

urlpatterns = [
    url(r'^$', views.certif_list, name="list"),
    url(r'^(?P<id>\d+)/$', views.certif_details, name="getCertif"),
]