#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Yampico is a web assistant for home management
#
# Copyright (C) 2012  Alberto Caso Palomino
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""URLs for Yampico root application

@author: Alberto Caso <alberto.caso@adaptia.es>

"""

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yampico.views.home', name='home'),
    # url(r'^yampico/', include('yampico.foo.urls')),

    # Enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Site's root
    url(r'^$', 'yampico.views.index'),

    # URLs from the Lists application.
    url(r'^lists/', include('yampico.lists.urls')),

    # URLs from the Dashboard application.
    url(r'^dashboard/', include('yampico.dashboard.urls')),
    
    # URLs from the Accounting application.
    url(r'^accounting/', include('yampico.accounting.urls')),
    
)

# Include support for static files
# TODO: In production, serve them from the web server and not from Django
urlpatterns += staticfiles_urlpatterns()

