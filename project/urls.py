from django.contrib import admin
from django.urls import path , include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-category/' , include('category.urls' , namespace = 'category')),
    path('api-meals/' , include('meals.urls' , namespace = 'meals')),
    path('api-accounts/' , include('accounts.urls' , namespace = 'accounts')),
    path('api-team/' , include('team.urls' , namespace = 'team')),
    path('api-booking/' , include('booking.urls' , namespace = 'booking')),
    path('api-testimonial/' , include('testimonial.urls' , namespace = 'testimonial')),
    path('api-contact/' , include('contact.urls' , namespace = 'contact')),
    path('api-token-auth/' , obtain_auth_token),
    
]
