from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),

    url(r'^$', 'getkernel.blog.views.blog'),
    url(r'^test_form/', 'getkernel.views.test_form'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)