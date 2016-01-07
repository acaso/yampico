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

"""Models for Yampico's Lists application.

"""

from django.db import models

import uuid

def generate_uuid():
    """Generates an UUID to be used as a record's ID."""
    # TODO: factor out to a common place
    return str(uuid.uuid4())

class List(models.Model):
    """List of things.
    
    This model represents a List of things.
    
    """
    
    id = models.CharField(max_length=128, primary_key=True, default=generate_uuid)
    """UUID for the list.
    
    We use an UUID for the id field to allow creating registers
    from different places and syncing afterwards.
    """

    name = models.CharField(max_length=150)
    """List's name."""
    
    description = models.CharField(max_length=250)
    """List's description."""

    def __unicode__(self):
        return self.name
    

class ListItem(models.Model):
    """List item.
    
    This model represents an item in a list.
    
    """
    
    id = models.CharField(max_length=128, primary_key=True, default=generate_uuid)
    """UUID for the list.
    
    We use an UUID for the id field to allow creating registers
    from different places and syncing afterwards.
    """

    description = models.CharField(max_length=500)
    """Item contents."""
    
    marked = models.BooleanField(default=False)
    """Flag to set an item as marked (checked)."""
    
    list = models.ForeignKey(List)
    """Parent list."""

    def __unicode__(self):
        return self.description



