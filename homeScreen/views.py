# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from homeScreen.models import *
from category.models import Category
from searchApp.models import Products, MetaData
# Create your views here.
from searchApp.models import CategoryItem
from django.utils.html import strip_tags
import html
import re

def clean_richtext_css(raw_html: str) -> str:
    if not raw_html:
        return ""

    # Remove HTML tags
    text = strip_tags(raw_html)

    # Convert &nbsp; → space
    text = html.unescape(text)

    # Remove multiple blank lines
    text = re.sub(r'\n\s*\n+', '\n', text)

    # Normalize indentation
    lines = [line.rstrip() for line in text.splitlines() if line.strip()]

    return "\n".join(lines)
def clean_richtext(value: str) -> str:
    """
    Convert RichTextField HTML content to clean plain text.

    - Removes HTML tags (<p>, <br>, etc)
    - Converts HTML entities (&nbsp; → space)
    - Trims extra whitespace
    """
    if not value:
        return ""

    text = strip_tags(value)      # remove HTML tags
    text = html.unescape(text)    # convert &nbsp;, &amp;, etc
    return text.strip()

def home_page(request):
    
    results = HomeConfig.objects.filter(status='active').order_by('rank')
    carouselSlide = Slide.objects.filter(status='active').order_by('rank')
    homePageContent = SectionContent.objects.filter(status='active').order_by('rank')
    meta_data = MetaData.objects.filter(textId='home').first()
    if not meta_data:
        meta_data, created = MetaData.objects.get_or_create(
            textId='home',
            defaults={
                'seoTitle': 'Home Page',
                'metaDescription': 'Welcome to our home page.',
                'canonicalUrl': '/',
                'breadcrumbTree': [],
                'status': 'y',
            }
        )

    carousel, product, categories, css_values, js_values, topContent_values, additional_values= '','', '', '', '', '', ''
    for row in results:
        # print('===',row.sectionType)
        if row.sectionType =='category':  
            rowData = clean_richtext(row.content)
            # print('clean_richtext:: ',rowData)  
            content_values = rowData.split(",")   
            print('----------------:: ',content_values)       
            values_string = ",".join("'{}'".format(value.strip()) for value in content_values)  # Enclose values in single quotes
            # print('values_string:: ',values_string)
            query = "SELECT * FROM `CategoryItem` WHERE textId IN ({})".format(values_string)
            categories = CategoryItem.objects.raw(query) 
            # for each in categories:
            #     print('each:', each.categoryImage)

        if row.sectionType =='series':  
            rowData = clean_richtext(row.content)
            # print('clean_richtext:: ',rowData)  
            content_values = rowData.split(",")   
            print('----------------:: ',content_values)       
            values_string = ",".join("'{}'".format(value.strip()) for value in content_values)  # Enclose values in single quotes
            # print('values_string:: ',values_string)
            query = "SELECT * FROM `CategoryItem` WHERE textId IN ({})".format(values_string)
            series_list = CategoryItem.objects.raw(query) 
            for each in series_list:
                print('each:', each.details)
  

        
        if row.sectionType =='product':  
            rowData = clean_richtext(row.content)
            content_values = rowData.replace(' ','').split(",")          
            values_string = ",".join("'{}'".format(value.strip()) for value in content_values)  # Enclose values in single quotes
            query = "SELECT * FROM `Products` WHERE productID IN ({})".format(values_string)
            product = Products.objects.raw(query)

        

          
            # for each in product:
            #     print('each:', each.productTitle)
            # print(products.__len__)
        

        if row.sectionType =='css':  
            css_values = clean_richtext_css(row.content)  

        if row.sectionType =='js':  
            js_values = row.content 

        if row.sectionType =='topContent':  
            topContent_values = row.content 

        if row.sectionType =='additional':  
            additional_values = row.content         

        if row.sectionType =='carousel':  
            carousel = row.content         
             
 


    return render(request, 'home.html',{'meta_data':meta_data,'homePageContent':homePageContent,'carouselSlide':carouselSlide, 'productData':product, 'categoryData':categories,'series_list':series_list, 'css':css_values,'js':js_values, 'additional':additional_values, 'topContent':topContent_values,'carousel':carousel }) 
    # return render(request, 'home.html', {'aQuery': query, 'productData': results})
