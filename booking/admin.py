from django.contrib import admin
from . models import BookTable
# Register your models here.


@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'no_of_people' , 'date_and_time']
    

