from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    textId = models.CharField(max_length=50, unique=True)
    categoryTitle = models.CharField(max_length=50, unique=True)
    parrentCategory = models.CharField(max_length=50, blank=True)
    description = RichTextField(blank=True)
    # categoryImage = models.TextField(blank=True)
    categoryImage = models.ImageField(upload_to='category/',blank=True, null=True) 
    breadcrumbTitle = models.CharField(max_length=100, blank=True)
    categoryUrl = models.CharField(max_length=100, blank=True)
    rank = models.IntegerField(default=0)  
    status = models.CharField(max_length=1, default='Y', blank=False)

    productCsv = models.TextField(blank=True, null=True)  # ✅ NEW COLUMN

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)

    def __str__(self):
        # return self.categoryTitle
        return f"{self.categoryTitle} ({self.productCsv})"
    
   

    class Meta:
        db_table = "Category"



    