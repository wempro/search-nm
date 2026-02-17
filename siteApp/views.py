from django.shortcuts import render, redirect
from django.http import HttpResponse
from siteApp.models import Product
 
from searchApp.models import Products, ProductItem, MetaData
from searchApp.utils import get_product_parent_tree

# from course.forms import ContactForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django import template
import json

register = template.Library()

@register.filter
def to_float(value):
    # Your conversion logic here
    return float(value)




 
     
def all_products(request,url=None):
    items = Products.objects.all()
    # if not items:
    #     return render(request, '404.html')
    meta_data = MetaData.objects.filter(textId='all-products').first()
    if not meta_data:
        tree=[{"name": "Show all products", "link": None}]
         

        meta_data, created = MetaData.objects.get_or_create(
            textId='all-products',
            defaults={
                'seoTitle': 'All Products list view',
                'metaDescription': 'Browse all products available on our platform.',
                'canonicalUrl': 'all-products',
                'breadcrumbTree': json.dumps(tree),
                'status': 'y',
            }
        )
    breadcrumb_tree = []
    if meta_data.breadcrumbTree:
        breadcrumb_tree = json.loads(meta_data.breadcrumbTree)
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 10)   
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'product_list.html', {'items':items,  'breadcrumb':breadcrumb_tree, 'meta_data':meta_data}) 

def productDetails(request,url):
    url = url
    print('url: ',url)
    breadcrumb_tree = []
    
    results = Products.objects.filter(searchUrl=url).first()
    if not results:
        if url not in ['category']:
            return render(request, '404.html')
        else:
            return redirect('all_categorries')
    # print('\\\\\ #### Category Tree:')
    meta_data = MetaData.objects.filter(textId=results.productID).first()
    if not meta_data:
        seo_title = f"{results.productTitle} | {results.brand}" if results.brand else results.productTitle
        tree = get_product_parent_tree(results.productID)
        
        meta_description = results.shortDescription if results.shortDescription else results.description
        
        if not meta_description:
            meta_description = results.description
            
        meta_data, created = MetaData.objects.get_or_create(
            textId=results.productID,
            defaults={
                'seoTitle': seo_title,
                'metaDescription': meta_description.strip()[:150],
                'canonicalUrl': results.productID,
                'breadcrumbTree': json.dumps(tree),
                'status': 'y',
            }
        )
        
    if meta_data.breadcrumbTree:
        breadcrumb_tree = json.loads(meta_data.breadcrumbTree)
    # print(results)
    # description = {'description': results.description }
    # additional1= { 'additional1' : results.additional1 }
    # additional2= { 'additional2' : results.additional2 }
    import ast
    additional3 = results.additional3

    data_list = ast.literal_eval(additional3)
     
    # for obj in additional3:
    #     print(obj)
    # tabData= { 'tabData' : results.tabData } 
        
    items = Products.objects.filter(productID__in=data_list)
    # for obj in items:
    #     print(obj.textId)
    results.additional3 = items
    print('count:', items.count())
    results.esUrl = results.esUrl if results.esUrl else "https://elementsearch.com/products/"+results.productID
    results.pniUrl = results.pniUrl if results.pniUrl else "https://pumpsandinstrumentations.com/search/"+results.productID


    # dd= {'description':description, 'additional1':additional1, 'additional2':additional2, 'additional3':additional3, 'tabData':tabData  }

    return render(request, 'product-details.html', {'data': results,  'breadcrumb':breadcrumb_tree, 'meta_data':meta_data, 'sidebar': False}) 
     

def search_results(request):
    search_text = request.GET.get('q', '')
    sData = str("%")+search_text.replace(" ", "%")+str("%")
    print(sData)
    # results = Products.objects.all()
    items = Products.objects.raw("SELECT *  FROM `Products` WHERE `productTitle` LIKE %s ", [sData])
    # data = Products.objects.all()

    # items_per_page = 10  # Define the number of items to display per page
    # paginator = Paginator(data, items_per_page)
    
     
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 10)   
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'search_results.html', {'query': search_text, 'items': items})

