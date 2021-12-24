from django.contrib import admin
from todolist.models import Task


class AdminTask(admin.ModelAdmin):
	list_display = ('tache', 'date_added')

admin.site.register(Task, AdminTask)
