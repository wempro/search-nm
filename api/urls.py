from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    # path('<slug:url>', views.productDetails, name='productDetails'),
         
    path('save/', views.api_save_product, name='api_save_product'),
    # path('<slug:url:url>', views.category, name='category'),
 
    # Add more URL patterns as needed.
]
