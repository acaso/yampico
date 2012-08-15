from django.db import models

class List(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name
    

class ListItem(models.Model):
    description = models.CharField(max_length=500)
    marked = models.BooleanField()
    list = models.ForeignKey(List)

    def __unicode__(self):
        return self.description



