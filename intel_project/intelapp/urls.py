__author__ = 'michal'
from django.conf.urls import patterns, url
from gameintelligence import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<number>\d+)$', views.index_with_number, name='index_with_number')
)
