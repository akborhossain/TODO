from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class AdminTask(admin.ModelAdmin):
    list_display=['title','description','created_at','due_date','updated_at', 'updated_by','username']
admin.site.register(Task, AdminTask)

class AdminRole(admin.ModelAdmin):
    list_display=['username','type']
admin.site.register(Role, AdminRole)