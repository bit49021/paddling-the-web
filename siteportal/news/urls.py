from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.article_detail, name="article_detail"),
]
