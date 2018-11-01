from django.conf.urls import url
from . import views

app_name = 'duminfo'

urlpatterns = [
    url(r'^form(?P<id>\d+)/$',views.updatedum, name = "singup"),
    url(r'^form(?P<id>\d+)/getForm$',views.viewPdf, name = "afsa"),
]