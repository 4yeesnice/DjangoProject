from django.contrib import admin
from .models import ToDo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', )


admin.site.register(ToDo, TodoAdmin)