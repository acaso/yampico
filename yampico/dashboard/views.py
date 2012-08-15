'''
Created on 11/08/2012

@author: alberto
'''
#!/usr/bin/env python

from django.shortcuts import render_to_response
#from django.http import HttpResponse
from django.http import HttpResponseRedirect

from lists.models import List, ListItem

def index(request):
    lists = List.objects.all()
    
    dashboard_data = {}
    
    dashboard_data['lists'] = lists
    
    return render_to_response('dashboard.html', dashboard_data)