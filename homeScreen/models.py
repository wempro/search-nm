from django.db import models 

from django.db.models import Model
from ckeditor.fields import RichTextField
class File(models.Model):
    file = models.FileField(upload_to='files')
     

class SectionContent(models.Model):
    textId = models.CharField(max_length=255, primary_key=True)  # Unique identifier
    sectionTitle = models.CharField(max_length=255)  # Heading for a specific section
    bodyContent = RichTextField(blank=True )  # Main content of the section
    # description = RichTextField(blank=True )
    css = RichTextField(blank=True )  # Optional custom CSS
    js = RichTextField(blank=True )  # Optional custom JavaScript
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])  # Section visibility
    rank = models.IntegerField(default=0)  # Numerical order for display
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.sectionTitle
    class Meta:
        db_table = "SectionContent" 
 

class HomeConfig(models.Model):
    sectionType = models.CharField(max_length=50, choices=[('carousel', 'Carousel'), ('category', 'Category List'),('product', 'Products List'),('series', 'Series List'),('css', 'Custome CSS'),('js', 'Custome JavaScript'),('topContent', 'Home Page Content'),('additional', 'Additional Content')])  
    rank = models.PositiveIntegerField()
    content = RichTextField(blank=True) 
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])  # Section visibility
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)


    def __str__(self):
        return f"{self.sectionType} ({self.rank})"

    class Meta:
        ordering = ['rank']
        db_table = "HomeConfig"  

class Slide(models.Model):
     # Assuming images are uploaded to 'slides/' directory
    title = models.CharField(max_length=100, unique=True)
    description = RichTextField(blank=True)
    image = models.ImageField(upload_to='slides/',blank=True, null=True) 
    rank = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')]) 
    #status = models.CharField(max_length=50, choices=[('left', 'Content shows Left to 60%'), ('right', 'Content shows Right to 60%'),('center', 'Content shows')])  
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.title} ({self.rank})"

    class Meta:
        ordering = ['rank']
        db_table = "Slide"  

