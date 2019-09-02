from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_intro, name="intro" ),
    url('^suggestions/$', views.index, name='homepage'),
    url(r'^signup/$', views.signup, name='signup'),   
    url(r'^new/image$', views.new_image, name='new-image'),
]