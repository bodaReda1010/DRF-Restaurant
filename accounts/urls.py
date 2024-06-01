from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('register/' , views.register , name = 'register'),
    path('get_info/' , views.get_info , name = 'get_info'),
    path('edit_profile/' , views.edit_profile , name = 'edit_profile'),
    path('reset_password/' , views.reset_password , name = 'reset_password'),

]