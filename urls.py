from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
	(r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
	
	url(r'^$', login),
    # url(r'^pysco/$', 'pysco.views.login'),
    
    url(r'^dashboard/', 'pysco.views.dashboard'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
