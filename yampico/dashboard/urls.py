'''
Created on 11/08/2012

@author: alberto
'''

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.index'),
)