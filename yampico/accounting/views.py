#!/usr/bin/env python
'''
Created on 25/08/2012

@author: alberto
'''

from django.shortcuts import render_to_response
#from django.http import HttpResponse
from django.http import HttpResponseRedirect

#from lists.models import List, ListItem

def index(request):
    
    return render_to_response('index.html')