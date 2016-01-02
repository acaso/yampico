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

"""Views for Yampico's Lists application

@author: Alberto Caso <alberto.caso@adaptia.es>

"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import ItemListForm
from .models import List, ListItem

def index(request):
    """Default action.
    
    Show the list of available lists.
    """
    
    lists_list = List.objects.order_by("id")

    return render(request, 'lists/index.html', {'lists': lists_list})

def detail(request, listid):
    """Show a list's items and details."""

    current_list = get_object_or_404(List, id=listid)
    
    return render(request, 'lists/list.html', {'current_list': current_list})
    

def add(request):
    """Add a list."""
    
    if request.method == 'POST' and request.POST.get('save', ''):
        # Request comes from the form and the user clicked on 'save' button
        
        form = ItemListForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            new_list = List(name=cd['name'], description=cd['description'])
            new_list.save()
            
            list_id = new_list.id
            
            return HttpResponseRedirect(reverse('lists.views.detail', args=(list_id,)))
        
    else:
        # Request does not come from the 'save' button. Just show the form.
        form = ItemListForm()
    
    return render(request, 'lists/list_form.html', {'form': form, 'action': 'add'})

def edit(request, listid):
    """Modify a list.
    
    Modify a list's generic data (ie. name or description).
    """
    
    my_list = get_object_or_404(List, id=listid)

    if request.method == 'POST' and request.POST.get('save', ''):
        # Request comes from the form and the user clicked on 'save' button

        form = ItemListForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
                        
            my_list.name = cd['name']
            my_list.description = cd['description']
            my_list.save()
            
            return HttpResponseRedirect(reverse('lists.views.index'))
    else:
        # Request is not a POST yet. Show the form with current data.
        form_data = {
            'name': my_list.name,
            'description': my_list.description,}
        form = ItemListForm(form_data)
        
    return render(request, 'lists/list_form.html', {'form': form, 'action': 'edit'})

def delete(request, listid):
    """Delete list."""
    
    my_list = get_object_or_404(List, id=listid)

    if request.method == 'POST' and request.POST.get('delete', None):
        # Request comes from the form that asks for confirmation and the
        # user clicked the 'yes' button.
        
        my_list.delete()
        return HttpResponseRedirect(reverse('lists.views.index'))
    
    else:
        # Ask for confirmation.
        return render(request, 'lists/delete_list_confirm.html', {'list': my_list})


def update_items(request, listid):
    """"Store items checked status.
    
    Store items checked status in the items list. User can check or uncheck
    several items and then click on 'update' to save those checks and unchecks.
    """

    if request.method == 'POST':
        
        selected_items = []
        
        # All items have name="list_items[]" so checked ones come packed
        # in an list named "list_items".
        for value in request.POST.getlist('list_items'):
            try:
                selected_items.append(value)
            except ValueError:
                # Ignore wrong values
                pass

        my_list = get_object_or_404(List, id=listid)

        # Get all items in the list from the DB to compare with the status
        # supplied in the form
        for list_item in my_list.listitem_set.all():
            if list_item.marked:
                # If set as marked in the DB but NOT set as marked
                # in the form, update the value in the DB
                if list_item.id not in selected_items:
                    list_item.marked = False
                    list_item.save()
            else:
                # If NOT set as marked in the DB but set as marked
                # in the form, update the value in the DB
                if list_item.id in selected_items:
                    list_item.marked = True
                    list_item.save()

        if request.POST.get('purge', None):
            # If button clicked was "Purge", proceed to purge this
            # list's checked items.
            my_list.listitem_set.filter(marked=True).delete()


    return HttpResponseRedirect(reverse('lists.views.detail', args=(listid,)))

def add_item(request, listid):
    """Add an item to a list."""

    my_list = get_object_or_404(List, id=listid)

    item_description = request.POST.get('description', None)

    if item_description:
        my_list.listitem_set.create(description = item_description)

    return HttpResponseRedirect(reverse('lists.views.detail', args=(listid,)))

def delete_item(request, itemid):
    """Delete an item from a list."""

    item = get_object_or_404(ListItem, id=itemid)

    if request.method == 'POST' and request.POST.get('delete', None):
        # Request is the result of clicking the 'yes' button on the
        # confirmation form.
        item.delete()
        return HttpResponseRedirect(reverse('lists.views.detail', args=(item.list.id,)))
    
    else:
        # Ask the user for confirmation
        return render(request, 'lists/delete_item_confirm.html', {'item': item})
