from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_intro, name="intro" ),
    url('^suggestions/$', views.index, name='homepage'),

]