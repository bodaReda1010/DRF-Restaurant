from rest_framework import serializers
from . models import Meal , Review


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['name' , 'category' , 'price' , 'created_at' , 'updated_at' , 'is_active']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user' , 'product' , 'rating' , 'comment']