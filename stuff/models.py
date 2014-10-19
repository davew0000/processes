from django.db import models

import datetime

from wf.models import Process

# Create your models here.

class first(models.Model):
    
    var_one = models.CharField(max_length=100)
    var_two = models.IntegerField()
    
    def __unicode__(self):
        return self.var_one + " " + unicode(self.var_two)
    
class second(models.Model):
    
    new_var_one = models.CharField(max_length=100)
    new_var_two = models.IntegerField()
    
    def __unicode__(self):
        return self.new_var_one + " " + unicode(self.new_var_two)
    
class Order(models.Model):
    
    date_raised = models.DateField(default=datetime.date.today())
    approved = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

