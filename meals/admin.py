from django.contrib import admin
from . models import Meal , Review
# Register your models here.



@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name' , 'category' , 'price' , 'created_at' , 'updated_at' , 'is_active']
    


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'rating' , 'comment']