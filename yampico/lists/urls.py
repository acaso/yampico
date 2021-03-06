# -*- coding: utf-8 -*-
#
# Yampico is a web assistant for home management
#
# Copyright (C) 2012-2016  Alberto Caso Palomino
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

"""URLs for Yampico's Lists application

@author: Alberto Caso <alberto.caso@adaptia.es>

"""

from django.conf.urls import url

from . import views

urlpatterns = [
    
    #URLs for managing lists themselves
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<listid>[0-9a-f\-]+)/$', views.detail, name='detail'),
    url(r'^(?P<listid>[0-9a-f\-]+)/edit/', views.edit, name='edit'),
    url(r'^(?P<listid>[0-9a-f\-]+)/delete/', views.delete, name='delete'),

    # URLs for managing the items of a list
    url(r'^(?P<listid>[0-9a-f\-]+)/update-items/$',
        views.update_items,
        name='update_items'),
    url(r'^(?P<listid>[0-9a-f\-]+)/add-item/$', views.add_item, name='add_item'),
    url(r'^[0-9a-f\-]+/delete-item/(?P<itemid>[0-9a-f\-]+)/$',
        views.delete_item,
        name='delete_item'),
]
