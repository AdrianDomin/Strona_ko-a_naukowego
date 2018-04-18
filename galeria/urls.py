from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.photo_list, name = 'photo_list'),
    url(r'^(?P<album_slug>[-\w]+)/$', views.photo_list, name = 'photo_list_by_album' ),

    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.photo_detail, name = 'photo_detail'),

]
