from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'intel_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^intel/', include('intelapp.urls', namespace='intelapp')),
    url(r'^admin/', include(admin.site.urls)),
)
