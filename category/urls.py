from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    # path('<slug:url>', views.productDetails, name='productDetails'), 

    path('', views.all_categorries, name='all_categorries'),
    # path('/', views.all_categorries, name='all_categorries'),
    path('<slug:url>', views.category_item, name='category_item'),

    # path('<slug:url:url>', views.category, name='category'),
 
    # Add more URL patterns as needed.
]
