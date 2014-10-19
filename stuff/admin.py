from django.contrib import admin

# Register your models here.
from .models import first, second

admin.site.register(first)
admin.site.register(second)