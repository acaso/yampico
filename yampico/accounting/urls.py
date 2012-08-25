from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('accounting.views',
    url(r'^$', 'index'),
)