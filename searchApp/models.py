from django.db import models 

from django.db.models import Model
from ckeditor.fields import RichTextField
class File(models.Model):
    file = models.FileField(upload_to='files')
    

class Products(models.Model):
    productID = models.CharField(max_length=50, unique=True)
    seriesID = models.CharField(max_length=50)
    productTitle = models.CharField(max_length=100, unique=True )
    searchUrl = models.CharField(max_length=100, unique=True )
    price = models.CharField(max_length=100, blank=True )
    shortDescription = models.TextField(blank=True, null=True, )
    description = RichTextField(blank=True )
    brand = models.CharField(max_length=100, blank=True, null=True)
    # description = models.TextField(blank=True )
    productImage = models.TextField(blank=True )
    esUrl = models.CharField(max_length=100, blank=True)
    pniUrl = models.CharField(max_length=100, blank=True)
    tabData = RichTextField(blank=True )
    rank = models.IntegerField(default=0) 
    # tabData = models.TextField(blank=True )
    additional1 = RichTextField(blank=True )
    # additional1 = models.TextField(blank=True )
    additional2 = RichTextField(blank=True )
    # additional2 = models.TextField(blank=True )
    additional3 = RichTextField(blank=True ) 
    # additional3 = models.TextField(blank=True ) 
    # categoryId = models.CharField(max_length=100, blank=True ) 
    # # breadcrumb = models.CharField(max_length=150, blank=True)
    # status = models.CharField(max_length=1, default='Y', blank=False)
    # status = models.CharField(max_length=5, choices=[('y', 'Y'), ('n', 'N')])
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(null=True)
       

    class Meta:
        db_table = "Products" 



# class HomePageContent(models.Model):
#     textId = models.CharField(max_length=255, primary_key=True)  # Unique identifier
#     sectionTitle = models.CharField(max_length=255)  # Heading for a specific section
#     bodyContent = RichTextField(blank=True )  # Main content of the section
#     css = RichTextField(blank=True )  # Optional custom CSS
#     js = RichTextField(blank=True )  # Optional custom JavaScript
#     status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])  # Section visibility
#     rank = models.IntegerField(default=0)  # Numerical order for display
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(null=True)

#     def __str__(self):
#         return self.sectionTitle

 

class CategoryItem(models.Model):
    textId = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=100)
    sub_title = models.TextField(blank=True, null=True)
    url = models.TextField(unique=True, max_length=100) 
    sourceUrl = models.TextField(unique=True, max_length=250) 
    brand = models.CharField(max_length=100, blank=True, null=True)
    parrent = models.TextField(max_length=100, default='root', blank=True) 
    type = models.CharField(max_length=15, choices=[('category', 'Category'),('sub-category', 'Sub Category'), ('pagination', 'Pagination'),('series', 'Series'),('root', 'Brand Root')], default='category')
    details = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=5, choices=[('y', 'Y'), ('n', 'N')])
    product_csv = models.TextField(blank=True, null=True)  
    rank = models.IntegerField(default=0)   
    series_csv = models.TextField(blank=True, null=True)  
    totalPageCount = models.IntegerField(blank=True, null=True)
    totalListPage = models.IntegerField(blank=True, null=True) 
    queryString = models.CharField(blank=True, max_length=50, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "CategoryItem" 

class SeriesItem(models.Model):
    textId = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=100)
    sub_title = models.TextField(blank=True, null=True)
    url = models.TextField( max_length=250) 
    type = models.CharField(max_length=15, choices=[('series', 'Series'), ('pagination', 'Pagination')], default='series')
    details = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=5, choices=[('y', 'Y'), ('n', 'N')])
    product_csv = models.TextField(blank=True, null=True)  
    category = models.TextField(blank=True, null=True)  
    rank = models.IntegerField(default=0)  
    brand = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "SeriesItem" 

class ProductItem(models.Model):
    title = models.CharField(max_length=100)
    textId = models.CharField(max_length=100, unique=True)
    url = models.TextField(unique=True,max_length=100 ) 
    sourceUrl = models.TextField(unique=True,max_length=250 ) 
    brand = models.CharField(max_length=100, blank=True, null=True)
    series = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    stock = models.TextField(blank=True, null=True)
    rank = models.IntegerField(default=0)   
    status = models.CharField(max_length=5, choices=[('y', 'Y'), ('n', 'N')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.textId})"
    
    class Meta:
        db_table = "ProductItem" 
  


class MetaData(models.Model):
    textId = models.CharField(max_length=100, unique=True)
    seoTitle = models.CharField(max_length=100)
    metaDescription = models.TextField(unique=True,max_length=250) 
    breadcrumbTree = models.TextField() 
    canonicalUrl = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=5, choices=[('y', 'Y'), ('n', 'N')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.seoTitle} ({self.textId})"
    
    class Meta:
        db_table = "MetaData" 

class Brand(models.Model):
    textId = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    shortDescription = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
     
    status = models.CharField(max_length=1, default='y')
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='brands/',blank=True, null=True) 

    def __str__(self):
        return f"{self.title} ({self.textId})"
    
    class Meta:
        db_table = "Brand" 