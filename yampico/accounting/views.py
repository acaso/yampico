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

"""Views for Yampico's Accounting application

@author: Alberto Caso <alberto.caso@adaptia.es>

"""

from django.shortcuts import render

from accounting.models import Account, Operation

def index(request):
    """Default action.
    
    Show accounts' balances and latests operations.
    
    """
    
    accounts_list = Account.objects.order_by("id")
    grand_balance = Account.get_grand_balance()
    
    # TODO: get only n latest operations and not all
    latest_operations = Operation.objects.all()

    return render(request, 'yampico.accounting/index.html',
        {'accounts': accounts_list,
         'grand_balance': grand_balance,
         'latest_operations': latest_operations})