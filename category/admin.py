from django.contrib import admin

# Register your models here.
from .models import  *


class CategoryAdmin(admin.ModelAdmin):
  
  # list_display = ('categoryTitle', "textId", 'categoryUrl', 'parrentCategory')
    list_display = ('textId', 'categoryTitle', 'parrentCategory', 'status', 'rank', 'productCsv')
    search_fields = ('categoryTitle', 'textId', 'productCsv')
    # list_filter = ('status',)
 

admin.site.register(Category, CategoryAdmin)

 

 
