#!/usr/bin/env python
'''
Created on 25/08/2012

@author: alberto
'''

from django.shortcuts import render_to_response
#from django.http import HttpResponse
from django.http import HttpResponseRedirect

#from lists.models import List, ListItem
from accounting.models import Account, Operation

def index(request):
    
    accounts_list = Account.objects.order_by("id")
    grand_balance = Account.get_grand_balance()
    
    latest_operations = Operation.objects.all()

    return render_to_response('yampico.accounting/index.html',
        {'accounts': accounts_list,
         'grand_balance': grand_balance,
         'latest_operations': latest_operations})