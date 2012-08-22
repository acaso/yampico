#!/usr/bin/env python

from django.shortcuts import render_to_response, get_object_or_404
#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from lists.models import List, ListItem

from lists.forms import ItemListForm

def index(request):
    lists_list = List.objects.order_by("id")

    return render_to_response('index.html', {'lists': lists_list})

def detail(request, listid):
    """
    Show a list's items and details
    """

    current_list = get_object_or_404(List, id=listid)
    
    return render_to_response('list.html', {'current_list': current_list})
    

def add(request):
    """
    Adds an item list
    """
    if request.method == 'POST' and request.POST.get('save', ''):
        form = ItemListForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            new_list = List(name=cd['name'], description=cd['description'])
            new_list.save()
            
            list_id = new_list.id
            
            return HttpResponseRedirect(reverse('lists.views.detail', args=(list_id,)))
        
    else:
        form = ItemListForm()
    
    return render_to_response('list_form.html', {'form': form, 'action': 'add'})

def edit(request, listid):
    """
    Modifies an item list
    """
    
    my_list = get_object_or_404(List, id=listid)

    if request.method == 'POST' and request.POST.get('save', ''):
        form = ItemListForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
                        
            my_list.name = cd['name']
            my_list.description = cd['description']
            my_list.save()
            
            return HttpResponseRedirect(reverse('lists.views.index'))
    else:
        form_data = {
            'name': my_list.name,
            'description': my_list.description,}
        form = ItemListForm(form_data)
        
    return render_to_response('list_form.html', {'form': form, 'action': 'edit'})

def delete(request, listid):
    """
    Delete list
    """
    
    my_list = get_object_or_404(List, id=listid)

    if request.method == 'POST' and request.POST.get('delete', None):
        my_list.delete()
        return HttpResponseRedirect(reverse('lists.views.index'))
    else:
        return render_to_response('delete_list_confirm.html', {'list': my_list})


def update_items(request, listid):

    if request.method == 'POST':
        
        selected_items = []
        for value in request.POST.getlist('list_items'):
            try:
                selected_items.append(value)
            except ValueError:
                # Ignore wrong values
                pass

        my_list = get_object_or_404(List, id=listid)

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
            # If button was Purge button, proceed to purge this list's marked items
            my_list.listitem_set.filter(marked=True).delete()


    return HttpResponseRedirect(reverse('lists.views.detail', args=(listid,)))

def add_item(request, listid):

    my_list = get_object_or_404(List, id=listid)

    item_description = request.POST.get('description', None)

    if item_description:
        my_list.listitem_set.create(description = item_description)

    return HttpResponseRedirect(reverse('lists.views.detail', args=(listid,)))

def delete_item(request, itemid):

    item = get_object_or_404(ListItem, id=itemid)

    if request.method == 'POST' and request.POST.get('delete', None):
        item.delete()
        #item.save()
        return HttpResponseRedirect(reverse('lists.views.detail', args=(item.list.id,)))
    else:
        return render_to_response('delete_item_confirm.html', {'item': item})

