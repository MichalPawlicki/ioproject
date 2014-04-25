from intelapp.views import RegisterView, SubmitFoeInfoView

__author__ = 'michal'
from django.conf.urls import patterns, url
from intelapp import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<number>\d+)$', views.index_with_number,
        name='index_with_number'),
    url(r'^register/?$', RegisterView.as_view(), name='register'),
    url(r'^register/confirm/(?P<code>\w{128})$', views.confirm_registration,
        name='confirm_registration'),
    url(r'^submit_info/?$', SubmitFoeInfoView.as_view(),
        name='submit_info'),
    url(r'^main$', views.main, name='main')
)

