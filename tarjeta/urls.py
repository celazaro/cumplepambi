
from django.urls import path
from tarjeta.views import home



urlpatterns = [
    
    path('', home, name='home')
]