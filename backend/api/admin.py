"""This is the init file for the api package."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):

   """This is the init file for the api package."""
    
    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
