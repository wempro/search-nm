
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import Q
import csv, io,os
from django.core.files.base import ContentFile
# from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import pandas as pd
from .models import Products, CategoryItem, ProductItem, SeriesItem
from django.http import JsonResponse, HttpResponse,FileResponse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
token ='Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MDAwMDAwMDAsInRva2VuX3R5cGUiOiJhY2Nlc3MifQ.XYZabc123FakeSignature'
import inspect

def clean_excel_value(value):
    """
    Handle Excel NaN / empty values safely
    """
    if pd.isna(value):
        return None
    return str(value).strip()
  

def productLoadByExtension(request):
     
    return redirect('home_page')        
         
def check_identity(data):
    print('check current url :', data)

    seri = SeriesItem.objects.filter(url=data).first()
    if seri:
        return seri
    pro = ProductItem.objects.filter(url=data).first()
    if pro:
        return pro
    cate = CategoryItem.objects.filter(url=data).first()
    if cate:
        return cate
    return False

def product_handler(currentUrl, data):
    print('call product_handler')
    required = ['productID', 'productTitle', 'searchUrl']
    missing = [f for f in required if not data.get(f)]
    if missing:
        return JsonResponse({'error': 'missing fields', 'missing': missing}, status=400)

    productID = str(data.get('productID')).strip()
    searchUrl = slugify(str(data.get('searchUrl')).strip())

    # check for existing records
    existing = Products.objects.filter(productID=productID).first()
    url_owner = Products.objects.filter(searchUrl=searchUrl).first()
    print('product created:', existing)

    if existing is None:
        if url_owner:
            return JsonResponse({'error': 'duplicate searchUrl', 'productID': url_owner.productID, 'searchUrl': url_owner.searchUrl}, status=400)
        
        
        print('_________________________create new with url__________________________')
        brand = currentUrl.brand if currentUrl else data.get('tabData', '')
        obj = Products.objects.create(
            productID = clean_excel_value(productID),
            brand= brand,
            productTitle = clean_excel_value(data.get('productTitle')),
            seriesID = clean_excel_value(data.get('seriesID','')),
            description = clean_excel_value(data.get('description', '')),
            price = str(data.get('price', '')).strip(),
            productImage = clean_excel_value(data.get('productImage', '')),
            searchUrl = clean_excel_value(searchUrl),
            shortDescription = clean_excel_value(data.get('shortDescription', '')),
            additional1 = clean_excel_value(data.get('additional1', '')),
            additional2 = clean_excel_value(data.get('additional2', '')),
            additional3 = clean_excel_value(data.get('additional3', '')),
            esUrl = clean_excel_value(data.get('esUrl', '')),
            pniUrl = clean_excel_value(data.get('pniUrl', '')),
            tabData = clean_excel_value(data.get('tabData', ''))
        )
        # return JsonResponse({'success': True, 'action': 'created', 'productID': obj.productID})
        
        get_next_page(currentUrl)
    else:
        get_next_page(currentUrl)
        # return JsonResponse({'error': 'Data not found'}, status=404)
    
def category_handler(currentUrl, data, brandName):
    print('call category_handler',currentUrl)
    if currentUrl:
        parrent = currentUrl.textId
        brand = currentUrl.brand
    else:
        parrent ='root'
        brand = brandName

    # saved_items = []
    for item in data:
        textId= slugify(item.get('title')),
        type = item.get('type', '')
        # print(item.get('title'),'____',textId,'___',brand,'___ ',item.get('url'),'------------',type)
        
        if type == 'series':
            
            SeriesItem.objects.get_or_create(
                textId= textId,
                defaults={
                'title': item.get('title', ''),
                'sub_title': item.get('subTitle', ''),
                'url':item.get('url', ''),
                'type':item.get('type', 'series'),
                'details': item.get('details', ''),
                'img': item.get('img', ''),
                'status': 'n',
                'category':parrent,
                'brand': brand or '',
                }
            )
        elif type == 'pagination':
            SeriesItem.objects.get_or_create(
                textId= textId,
                defaults={
                'title': currentUrl.title or item.get('title', ''),
                'brand': brand or '',
                'sub_title': item.get('subTitle', ''),
                'url':item.get('url', ''),
                'type':item.get('type', 'pagination'),
                'details': item.get('details', ''),
                'img': item.get('img', ''),
                'status': 'n',
                'category':parrent,
 
                }
            )
      
        elif type == 'category':
            status = 'n' if item.get('url') else 'y'
            print('category::: ',item.get('title'),'____',textId,'___',brand,'___ ',item.get('url'),'------------',type)
            CategoryItem.objects.get_or_create(
                textId= slugify(item.get('title')),
                
                defaults={
                'title': item.get('title', ''),
                'sub_title': item.get('subTitle', ''),
                'url':item.get('url', ''),
                'parrent':parrent,
                'type':item.get('type', 'category'),
                'details': item.get('details', ''),
                'img': item.get('img', ''),
                'status': status,
                'brand': brand or '',
                }
            )
            seriseData = item.get('series')
            # category= slugify(item.get('title'))
            if seriseData:
                # print('item.series_______________________ ',item.get('series'))
                for each in seriseData:
                    # print('_______________________ ',each.get('url'))
                    print(each.get('title'),'____',textId,'___',brand,'___ ',each.get('url'),'------------',type)
                    SeriesItem.objects.get_or_create(
                        textId= slugify(each.get('title')),
                        # url=each.get('url', ''),
                        defaults={
                        'title': each.get('title', ''),
                        'url': each.get('url', ''),
                        'sub_title': each.get('subTitle', ''),
                        'type':each.get('type', 'series'),
                        'details': each.get('details', ''),
                        'img': each.get('img', ''),
                        'status': 'n',
                        'category':slugify(item.get('title')),
                        'brand': brand or '',
                        }
                    )
                  

                     

                    # print('item.series_______________________ ',each.get('title'))



    # saved_items.append(obj.id)
    
    if item.get('type')=='category':
        url = CategoryItem.objects.exclude(status='y').values_list('url', flat=True).first()
        
        print(f"Line no: {inspect.currentframe().f_lineno}", url, '____')

        return JsonResponse({'success': True, 'next': url})

    # return JsonResponse({'error': 'Data not found'}, status=404)

def product_list_handler(currentUrl, data):
    if currentUrl:
        category = currentUrl.category
        brand = currentUrl.brand
        textId = currentUrl.textId
       
    print('call product_list_handler')
    # up=CategoryItem.objects.filter(url=currentUrl.url).update( status='y')
    # print('updated category url status:', up)
    # url = CategoryItem.objects.exclude(status='y').values_list('url', flat=True).first()

 
    for item in data:
        print('_________________currentUrl:', currentUrl.url)
        # cate = CategoryItem.objects.filter(url=currentUrl.url).first()
        ProductItem.objects.get_or_create(
            textId=item.get('ProductId'),
            defaults={
                'title': item.get('title', ''),
                'url': item.get('url', ''),
                'brand': item.get('brand', '') or brand,
                'img': item.get('img', ''),
                'stock': item.get('stock', ''),
                'status': 'n',
                'category': category,
                'series': textId
            }
        )
    get_next_page(currentUrl)
    # saved_items.append(obj.id)
    # return JsonResponse({'success': True, 'action': 'updated', 'next': url})
    # return JsonResponse({'error': 'Data not found'}, status=404)
    
@csrf_exempt
def api_save_product(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION') 
 
    if not auth_header or auth_header != token:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception as e:
        return JsonResponse({'error': 'invalid JSON', 'details': str(e)}, status=400)
    
    # if isinstance(data, list):
    category = data.get('category')
    productList = data.get('productList')
    productData = data.get('productData')
    current= data.get('currentUrl')
    brandName= data.get('brand')

    print('currentUrl received:', current)
 
    current_page = check_identity(current)

    returnData = None

    if category:
        returnData= category_handler(current_page, category, brandName)
    if productList:
        # print('product list found', productList)
        returnData= product_list_handler(current_page, productList)
    if productData:
        returnData= product_handler(current_page, productData)

    
    if returnData is not None:
        print('data is not None:', returnData)
        return  returnData
    else:
        print(f"Line no: {inspect.currentframe().f_lineno}",  'data not found')
        return get_next_page(current_page)
    # return JsonResponse({'success': True, 'action': 'updated', })

def get_next_page(currentUrl):
    if currentUrl:
        CategoryItem.objects.filter(url=currentUrl.url).update( status='y')
    url = CategoryItem.objects.exclude(status='y').values_list('url', flat=True).first()
    if url:
        print('next category url found:', url)
        return JsonResponse({'success': True, 'next': url})
    
    if currentUrl:
        SeriesItem.objects.filter(url=currentUrl.url).update( status='y')
    url = SeriesItem.objects.exclude(status='y').values_list('url', flat=True).first()
    if url:
        print('next product url found:', url)
        return JsonResponse({'success': True, 'next': url})
    
    if currentUrl:
        ProductItem.objects.filter(url=currentUrl.url).update( status='y')
    url = ProductItem.objects.exclude(status='y').values_list('url', flat=True).first()
    if url:
        print('next product url found:', url)
        return JsonResponse({'success': True, 'next': url})
    
    return JsonResponse(
        {
            'success': False,
            'message': 'No more URLs to process'
        },
        status=200
    )  

 





