from django.contrib import admin

# Register your models here.
from .models import Workflow, Node, Transition, Process, Task

admin.site.register(Workflow)
admin.site.register(Node)
admin.site.register(Transition)
admin.site.register(Process)
admin.site.register(Task)