from django.urls import path
from . import views
# from category.views import all_categorries
from category.views import all_categorries, category_item
urlpatterns = [
    
    path('all-products', views.all_products, name='all_products'),
   
  
    path('search', views.all_products, name='all_products'),
    path('search/', views.search_results, name='search_results'),
    
    path('<slug:url>', views.productDetails, name='productDetails'),


 
    # Add more URL patterns as needed.
]
