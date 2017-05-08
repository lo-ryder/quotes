from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.posts, name='posts'),
    url(r'^main$', views.contribute, name='contribute'),
    url(r'^$', views.quotes, name='quotes'),
]
