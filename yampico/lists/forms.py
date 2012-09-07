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

"""Forms for Yampico's Lists application.

"""

from django import forms

class ItemListForm(forms.Form):
    """Form to create/modify a list's generic data.
    
    This form allows the user to define or modify the generic data
    of a list (ie. its name or description).
    Note that this form is not used for managing the list's items.
     
    """
    
    name = forms.CharField()
    """List's name.
    
    Associated with name field of the List model."""
    
    description = forms.CharField(required=False)
    """List's description.
    
    Associated with description field of the List model."""
