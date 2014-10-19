from django.db import models
from django.db.models.loading import get_model
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

import json
import datetime

class Workflow(models.Model):
    
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    
    name = models.CharField(max_length=100)
    module = models.CharField(max_length=50, null=True, blank=True)
    function = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    def execute(self, *args, **kwargs):
        """Execute the function given in the data record attributes"""
        
        # Get the module
        m = __import__(self.module)
        
        # Not sure why I have to do this, but it only seems to load the bottom level module
        # So I loop through all subsequent modules and load them into variable 'att'
        modules = self.module.split(".")
        for module in modules[1:] :
            att = getattr(m, module)
        
        # Get the function
        function = getattr(att, self.function)
        
        # Execute the function with **kwargs
        return function(*args, **kwargs)
    
    def complete(self, models):
        models
    
class Node(models.Model):
    
    workflow = models.ForeignKey(Workflow)
    
    name = models.CharField(max_length=100)
    task = models.ForeignKey(Task)
    
    start_node = models.BooleanField(default=False)
    terminal_node = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
    
class Transition(models.Model):
    
    from_node = models.ForeignKey(Node, related_name="from")
    to_node = models.ForeignKey(Node, related_name="to")
    index = models.IntegerField(default=1 )
    
    def __unicode__(self):
        return unicode(self.from_node) + " to " + unicode(self.to_node)
    
class Process(models.Model):
    
    model_set = models.TextField(null=True, blank=True)
    current_node = models.ForeignKey(Node, null=True, blank=True)
    date_initiated = models.DateField(default=datetime.date.today())
    transition_ready = models.BooleanField(default=False)
    
    def __unicode__(self):
        return unicode(self.id)
    
    def write_models(self, models):
        """Writes a set of models as a json string to the model_set attribute"""
        
        model_list = []
        for model in models :
            name = model.__class__.__name__
            app = model._meta.app_label
            id = model.id
            model_list.append({ "name" : name, "app" : app, "id" : id })
            
        self.model_set = json.dumps(model_list)
        self.save()
        
    def load_models(self):
        """Loads a set of models from the json string in the database"""
        
        model_set = json.loads(self.model_set)
        
        records = []
        for item in model_set :
            model = get_model(item["app"], item["name"])
            records.append(model.objects.get(id=item["id"]))
        return records
    
    def progress(self):
            outcome = self.current_node.task.execute(self.load_models())
            try :
                transition = Transition.objects.get(from_node=self.current_node, index=outcome)
            except ObjectDoesNotExist :
                return False
            self.current_node = transition.to_node
            self.transition_ready = False
            self.save()
            return True
        
    def run(self):
        while self.progress() :
            pass
                
        