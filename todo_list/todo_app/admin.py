from django.contrib import admin
from .models import ToDoList, ToDoItem

admin.site.register(ToDoList)
admin.site.register(ToDoItem)

# Register your models here.
