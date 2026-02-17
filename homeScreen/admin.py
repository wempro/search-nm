from django.contrib import admin

# Register your models here.
from .models import  *
# from siteApp.models import  *


class SectionContentAdmin(admin.ModelAdmin):
    list_display = ("textId", 'sectionTitle', 'status','rank')
 

class HomeConfigAdmin(admin.ModelAdmin):
    list_display = ('sectionType', "id", 'status','rank')

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', "id", 'status','rank')
 

admin.site.register(SectionContent, SectionContentAdmin)
admin.site.register(HomeConfig, HomeConfigAdmin)
admin.site.register(Slide, SlideAdmin)
 
 
