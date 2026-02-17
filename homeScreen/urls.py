from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'), 


 
    # Add more URL patterns as needed.
]
