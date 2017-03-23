from django.conf.urls import url

from books import views

urlpatterns = [
    url(r'^search/$', views.search),
]
