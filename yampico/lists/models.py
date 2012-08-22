from django.db import models

import uuid

def generate_uuid():
    return str(uuid.uuid4())

class List(models.Model):
    id = models.CharField(max_length=128, primary_key=True, default=generate_uuid)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name
    

class ListItem(models.Model):
    id = models.CharField(max_length=128, primary_key=True, default=generate_uuid)
    description = models.CharField(max_length=500)
    marked = models.BooleanField()
    list = models.ForeignKey(List)

    def __unicode__(self):
        return self.description



