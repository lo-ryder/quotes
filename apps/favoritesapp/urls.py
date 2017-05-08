from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^removequote/(?P<id>\d+)$', views.removequote, name='removequote'),
    url(r'^addquote/(?P<id>\d+)$', views.addquote, name='addquote'),
]
