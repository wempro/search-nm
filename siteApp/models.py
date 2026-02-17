from django.db import models 

from django.db.models import Model
from ckeditor.fields import RichTextField
 

class Product(models.Model):
    productID = models.CharField(max_length=50, unique=True)
    # seriesID = models.CharField(max_length=50, unique=True)
    # productTitle = models.CharField(max_length=255, unique=True)
    # searchUrl = models.CharField(max_length=100, unique=True)
    # price = models.CharField(max_length=100, blank=True)
    # shortDescription = models.CharField(max_length=255, blank=True)
    # description = models.TextField(blank=True)
    # productImage = models.TextField(blank=True)
    # esUrl = models.CharField(max_length=100, blank=True)
    # pniUrl = models.CharField(max_length=100, blank=True)
    # tabData = models.TextField(max_length=100, blank=True)
    # additional1 = models.TextField(blank=True)
    # additional2 = models.TextField(blank=True)
    # additional3 = models.TextField(blank=True) 
    # # breadcrumb = models.CharField(max_length=150, blank=True)
    # # status = models.CharField(max_length=1, default='Y', blank=False)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(null=True)
       

    class Meta:
        db_table = "Product" 
 

