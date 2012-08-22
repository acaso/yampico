from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('lists.views',
    url(r'^$', 'index'),
    url(r'^add/$', 'add'),
    url(r'^(?P<listid>[0-9a-f\-]+)/$', 'detail'),
    url(r'^(?P<listid>[0-9a-f\-]+)/edit/', 'edit'),
    url(r'^(?P<listid>[0-9a-f\-]+)/delete/', 'delete'),

    url(r'^(?P<listid>[0-9a-f\-]+)/update-items/$', 'update_items'),
    url(r'^(?P<listid>[0-9a-f\-]+)/add-item/$', 'add_item'),
    url(r'^[0-9a-f\-]+/delete-item/(?P<itemid>[0-9a-f\-]+)/$', 'delete_item'),
)