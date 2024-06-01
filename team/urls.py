from django.urls import path
from . import views

app_name = 'team'


urlpatterns = [

    path('team/' , views.team , name = 'team'),
    path('team_id/<str:id>/' , views.team_id , name = 'team_id'),

]
