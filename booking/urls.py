from django.urls import path
from . import views

app_name = 'booking'


urlpatterns = [

    path('booking/' , views.booking , name = 'booking'),
    path('booking_id/<str:id>/' , views.booking_id , name = 'booking_id'),

]