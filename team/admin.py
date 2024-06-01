from django.contrib import admin
from . models import Chef
# Register your models here.



@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['name' , 'job_title']
    
