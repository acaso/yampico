'''
Created on 11/08/2012

@author: alberto
'''
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('dashboard/')