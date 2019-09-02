from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_intro, name="intro" ),
    url('^suggestions/$', views.index, name='homepage'),
    url(r'^signup/$', views.signup, name='signup'),   
    url(r'^new/image$', views.new_image, name='new-image'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)