from django.contrib import admin

# Register your models here.
from .models import  *
# from siteApp.models import  *


class ProductsAdmin(admin.ModelAdmin):
  
  list_display = ("productID", 'productTitle', 'searchUrl','price')
  search_fields   = ('productTitle','productID')
 

# class HomePageContentAdmin(admin.ModelAdmin):
#     list_display = ("textId", 'sectionTitle', 'status','rank')


class CategoryItemAdmin(admin.ModelAdmin):
    list_display = ( "textId",  'type', 'sourceUrl', 'parrent','sub_title','product_csv','status','rank')
    search_fields   = ('textId','title','type')
    # list_per_page = 50
    # filter = ('textId','title','type')

class ProductItemAdmin(admin.ModelAdmin):
    list_display = ( "textId", 'title', 'sourceUrl', 'status','category')
    search_fields   = ('textId','title','type')

class MetaDataAdmin(admin.ModelAdmin):
    list_display = ( 'textId', 'seoTitle',  'metaDescription','breadcrumbTree','canonicalUrl','status')
    search_fields   = ('textId','seoTitle','metaDescription')
    # list_per_page = 50
    # filter = ('textId','title','type')

# admin.site.register(HomePageContent, HomePageContentAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(CategoryItem, CategoryItemAdmin)
admin.site.register(MetaData, MetaDataAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
 

 


# class SectionContentAdmin(admin.ModelAdmin):
#     list_display = ("textId", 'sectionTitle', 'status','rank')
 

# class HomeConfigAdmin(admin.ModelAdmin):
#     list_display = ('sectionType', "id", 'status','rank')

# class SlideAdmin(admin.ModelAdmin):
#     list_display = ('title', "id", 'status','rank')
 

# admin.site.register(SectionContent, SectionContentAdmin)
# admin.site.register(HomeConfig, HomeConfigAdmin)
# admin.site.register(Slide, SlideAdmin)
 
 
