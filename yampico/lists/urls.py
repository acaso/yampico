from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('lists.views',
    url(r'^$', 'index'),
    url(r'^(?P<listid>\d+)/$', 'detail'),
    url(r'^add/$', 'lists.views.add'),
    url(r'^(?P<listid>\d+)/edit/', 'edit'),
    url(r'^(?P<listid>\d+)/delete/', 'delete'),

    url(r'^(?P<listid>\d+)/update-items/$', 'update_items'),
    url(r'^(?P<listid>\d+)/add-item/$', 'add_item'),
    url(r'^\d+/delete-item/(?P<itemid>\d+)/$', 'delete_item'),
)