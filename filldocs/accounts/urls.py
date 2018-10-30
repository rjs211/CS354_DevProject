from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$',views.signup_view, name = "singup"),
    url(r'^dummy/$',views.dummy_view, name = "dummy"),
    url(r'^login/$',views.login_view, name = "login"),
    url(r'^logout/$', views.logout_view, name="logout"),
]