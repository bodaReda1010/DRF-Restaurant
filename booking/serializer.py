from rest_framework import serializers
from . models import BookTable

class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = ['email' , 'no_of_people' , 'date_and_time']
