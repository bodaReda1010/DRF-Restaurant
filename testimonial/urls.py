from django.urls import path
from . import views

app_name = 'testimonial'


urlpatterns = [

    path('testimonial/' , views.comment , name = 'comment'),
    path('testimonial_id/<str:id>/' , views.comment_id , name = 'comment_id'),

]


