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

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

@author: Alberto Caso <alberto.caso@adaptia.es>

"""

from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'yampico.views.home', name='home'),
    # url(r'^yampico/', include('yampico.foo.urls')),

    # Enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Site's root
    url(r'^$', views.index, name='index'),

    # URLs from the Lists application.
    url(r'^lists/', include('lists.urls')),

    # URLs from the Dashboard application.
    url(r'^dashboard/', include('dashboard.urls')),
    
    # URLs from the Accounting application.
    url(r'^accounting/', include('accounting.urls')),
    
]
