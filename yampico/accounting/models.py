from django.db import models
import decimal

import uuid

def generate_uuid():
    return str(uuid.uuid4())


class Operation(models.Model):
    id = models.CharField(max_length=128, primary_key=True, default=generate_uuid)
    date = models.DateField()
    description = models.CharField(max_length=250)
    balance = models.DecimalField(decimal_places=2, max_digits=30)
    
    def __unicode__(self):
        return self.description
    
    
class Account(models.Model):
    id = models.CharField(max_length=128, primary_key=True, default=generate_uuid)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    balance = models.DecimalField(decimal_places=2, max_digits=30)
    operations = models.ManyToManyField(Operation, through='AccountOperations')
    
    @classmethod
    def get_grand_balance(cls):
        '''
        Return total balance
        '''
        
        balance = decimal.Decimal(0)
        accounts = cls.objects.all()
        for account in accounts:
            balance = balance + account.balance
        
        return balance

    def __unicode__(self):
        return self.name


class AccountOperations(models.Model):
    account = models.ForeignKey(Account)
    operation = models.ForeignKey(Operation)
    amount = models.DecimalField(decimal_places=2, max_digits=30)