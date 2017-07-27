from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.newlunch, name='newlunch'),
    url(r'^index', views.index, name='index'),
    url(r'^home', views.home, name='home'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', views.Login, name='login'),
]
