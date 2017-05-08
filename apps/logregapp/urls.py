from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^main$', views.main, name='main'),
    url(r'^$', views.index, name='index'),
]
