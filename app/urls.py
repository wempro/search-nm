 
from django.contrib import admin
from django.urls import path, include
from django.urls import path, include  
from searchApp import views
# from category.views import all_categorries, category_item
from django.conf import settings
from django.conf.urls.static import static




 

urlpatterns = [
    path("admin/", admin.site.urls), 
    path('dashboard/', include('searchApp.urls')),

    # path('category', all_categorries, name='all_categorries'),
    # path('category/', all_categorries, name='all_categorries'),
    # path('category/<slug:url>', category_item, name='category_item'),
    path('category/', include('category.urls')),

    # path('api/', include('api.urls')),
    path('api/save/', views.api_save_product, name='api_save_product'),
    path('', include('homeScreen.urls')),
    path('', include('siteApp.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)