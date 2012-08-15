'''
Created on 11/08/2012

@author: alberto
'''
from django import forms

class ItemListForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(required=False)
    
    