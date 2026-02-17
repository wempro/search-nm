from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('/hh', views.home_page, name='home_page'),
    path('', views.csvUpload, name='adminHome'),
    # path('user', admin.site.urls),
    path('login', views.LoginView, name='LoginView'),
    # path('logout', views.logoutView, name='logoutView'),
    path('success', views.success_page, name='success_page'),
    path('logout', views.logoutView, name='logoutView'),
  
    path('product-upload', views.csvUpload, name='productUpload'),
    path('delete/', views.deleteProduct, name='deleteProduct'),
    path('export/', views.dadaExport, name='dadaExport'),
    path('search/', views.search, name='adminSearch'),
    path('download-files/', views.download_and_file_management, name='download_and_file_management'),

    
    # path('/', views.LoginView.as_view(template_name="login.html"), name='login')
]
