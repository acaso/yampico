from django.contrib import admin
from accounting.models import Account, Operation

admin.site.register(Account)
admin.site.register(Operation)
