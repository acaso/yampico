from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yampico.views.home', name='home'),
    # url(r'^yampico/', include('yampico.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'yampico.views.index'),
    url(r'^lists/', include('yampico.lists.urls')),

    url(r'^dashboard/', include('yampico.dashboard.urls')),
    
    url(r'^accounting/', include('yampico.accounting.urls')),
    
)

urlpatterns += staticfiles_urlpatterns()

