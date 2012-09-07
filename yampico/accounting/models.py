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

"""Models for Yampico's accounting application.

"""

from django.db import models
import decimal

import uuid

def generate_uuid():
    """Generates an UUID to be used as a record's ID."""
    # TODO: factor out to a common place
    return str(uuid.uuid4())


class Operation(models.Model):
    """Accounting operation.
    
    This model represents an accounting operation, which can involve one
    or more accounts. It is associated with the Account model through
    the AccountOperations model.
    """
    
    id = models.CharField(max_length=128, primary_key=True,
                          default=generate_uuid)
    """UUID for the operation.
    
    We use an UUID for the id field to allow creating registers
    from different places and syncing afterwards.
    """
    
    date = models.DateField()
    """Operation's date."""
    
    description = models.CharField(max_length=250)
    """Operation's textual description."""

    balance = models.DecimalField(decimal_places=2, max_digits=30)
    """Net balance of this operation."""
    """
    This is redundant with the partial amount associated with each
    involved account (stored in the 'amount' field of AccountOperations
    model, but this allows to calculate it only on creation and
    modifications and not on every view.
    """     
    
    def __unicode__(self):
        return self.description
    
    
class Account(models.Model):
    """Account model.
    
    This model represents an account. It is associated with the Operation 
    model through the AccountOperations model.
    """
    
    id = models.CharField(max_length=128, primary_key=True, default=generate_uuid)
    """UUID for the account.

    We use an UUID for the id field to allow creating registers
    from different places and syncing afterwards.
    """

    name = models.CharField(max_length=150)
    """Account's name."""
    
    description = models.CharField(max_length=250)
    """Account's long description."""
    
    balance = models.DecimalField(decimal_places=2, max_digits=30)
    """Current balance for this account."""
    """
    This is redundant with the partial amount associated with each
    involved operation (stored in the 'amount' field of AccountOperations
    model, but this allows to calculate it only on creation and
    modifications and not on every view.
    """
    
    operations = models.ManyToManyField(Operation, through='AccountOperations')
    """ManyToMany link to Operation model."""
    
    @classmethod
    def get_grand_balance(cls):
        """Return total balance (sum of all accounts' balances)."""
        
        # Use a decimal type to ensure exact precision
        balance = decimal.Decimal(0)
        accounts = cls.objects.all()
        for account in accounts:
            balance = balance + account.balance
        
        return balance

    def __unicode__(self):
        return self.name


class AccountOperations(models.Model):
    """Aux model to represent Account and Operation's ManyToMany
    relationship."""
    
    account = models.ForeignKey(Account)
    operation = models.ForeignKey(Operation)
    amount = models.DecimalField(decimal_places=2, max_digits=30)
    """Money amount involved in the operation for this account."""
