from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'lists.views.index'),
    url(r'^(?P<listid>\d+)/$', 'lists.views.detail'),
    url(r'^add/$', 'lists.views.add'),
    url(r'^(?P<listid>\d+)/edit/', 'lists.views.edit'),
    url(r'^(?P<listid>\d+)/delete/', 'lists.views.delete'),

    url(r'^(?P<listid>\d+)/update-items/$', 'lists.views.update_items'),
    url(r'^(?P<listid>\d+)/add-item/$', 'lists.views.add_item'),
    url(r'^\d+/delete-item/(?P<itemid>\d+)/$', 'lists.views.delete_item'),
)