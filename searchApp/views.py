
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm,CSVUploadForm
from django.db.models import Q
import csv, io,os
from django.core.files.base import ContentFile
# from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import pandas as pd
from .models import Products, CategoryItem, ProductItem, SeriesItem, Brand
from django.http import JsonResponse, HttpResponse,FileResponse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
 
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
token ='Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MDAwMDAwMDAsInRva2VuX3R5cGUiOiJhY2Nlc3MifQ.XYZabc123FakeSignature'
import inspect
from django.forms.models import model_to_dict
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, parse_qsl, quote_plus
from searchApp.utils import get_category_parent_tree, download_and_save_image, process_additional_html

brand_obj = None
def clean_excel_value(value):
    """
    Handle Excel NaN / empty values safely
    """
    if pd.isna(value):
        return None
    return str(value).strip()



def remove_last_page_param(url, allowed_params=('p', 'pPgNo')):
    parsed = urlparse(url)
    query_list = parse_qsl(parsed.query, keep_blank_values=True)

    if not query_list:
        return url

    last_key, last_value = query_list[-1]

    # only remove if last param matches condition
    if last_key in allowed_params and last_value.isdigit():
        query_list.pop()

    new_query = urlencode(query_list, doseq=True)
    return urlunparse(parsed._replace(query=new_query))
def remove_query_param(url, param_name):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    # remove param if exists
    query.pop(param_name, None)

    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

def build_page_url(base_url, page_no, query_key):
    parsed = urlparse(base_url)
    query = parse_qs(parsed.query)

    # sanitize query key
    query_key = query_key.lstrip('&?')

    query[query_key] = [str(page_no)]
    new_query = urlencode(query, doseq=True)

    return urlunparse(parsed._replace(query=new_query))


def LoginView(request):
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or perform other actions
                return redirect('/')
    
    else:
        if request.user.is_authenticated:
            # return render(request, 'csv-upload.html') 
            redirect('/')
        else:
            form = UserLoginForm()

    return render(request, 'login.html')

 
def success_page(request):
    return render(request, 'login-success.html',{'sidebar': False}) 
 
def logoutView(request):
    logout(request)
    print(request.user)
    return redirect('/')
 
def deleteProduct(request):
    if request.user.is_authenticated:  
        qAll = request.GET.get('by', '')
        byQuery = request.GET.get('qu', '')
        print(qAll)
        print(byQuery)
        if qAll == 'search':
            # words = byQuery.split()
            # q_objects = Q()
            # for word in words:
            #     q_objects |= Q(productTitle__icontains=word)

            # results = Products.objects.filter(q_objects)
            results = Products.objects.filter(productTitle__icontains=byQuery)
            # return redirect('/')
            # sQuery = str("%")+byQuery.replace(" ", "%")+str("%") 
            # objs = Products.objects.raw("SELECT id  FROM `Products` WHERE `productTitle` LIKE %s ", [sQuery])
            results.delete()
            print('-------------search-----------')
        elif qAll == 'all':
            Products.objects.all().delete()
            print('elseeeeeeeeeeee')
            # Products.objects.raw("TRUNCATE TABLE `searchdb`.`products`")
        else:
            print(byQuery)
            print("-------------iproductID----------------")
            results=Products.objects.filter(productID=byQuery)
            results.delete()
            print("data")
        # if data == '':
        return redirect('productUpload')
    else:
        return redirect('home_page')
def download_and_file_management(request):
    Category_list = CategoryItem.objects.filter(status='y', img__startswith='https')

    for c_item in Category_list:
        if c_item and c_item.img:   
            local_path = download_and_save_image(
                c_item.img,
                c_item,
                'img',  
                f"{c_item.brand}/category"
            )

    product_list = ProductItem.objects.filter(status='y', img__startswith='https')
 


    for p_item in product_list:
        if p_item and p_item.img:    
            local_path = download_and_save_image(
                p_item.img,
                p_item,
                'img',  
                f"{p_item.brand}/product_list"
            )

    product_item = Products.objects.filter(
        Q(productImage__startswith='https') |
        Q(productImage__startswith='//') |
        Q(additional2__gt='')
    )

    for p_item in product_item:
        if p_item and p_item.productImage:  
            local_path = download_and_save_image(
                p_item.productImage,
                p_item,
                'productImage',  
                f"{p_item.brand}/products"
            )
        # if p_item.additional1:
        #     updated_html = process_additional_html(
        #         p_item.additional1,
        #         p_item.brand
        #     )

        #     if updated_html != p_item.additional1:
        #         p_item.additional1 = updated_html
        #         p_item.save(update_fields=['additional1'])

        #         print('PDF updated for product:', p_item.id)
    return render(request, 'file-save-loding.html')

def search(request):
    if request.user.is_authenticated:  
        query = request.GET.get('ad', '')
        words = query.split()
        q_objects = Q()
        for word in words:
            q_objects |= Q(productTitle__icontains=word)
        # results = Products.objects.filter(q_objects)
        results = Products.objects.filter(productTitle__icontains=query)
        
        # sData = str("%")+query.replace(" ", "%")+str("%")
        # results = Products.objects.all()
        # results = Products.objects.raw("SELECT *  FROM `Products` WHERE `productTitle` LIKE %s ", [sData])
        return render(request, 'admin-search.html', {'aQuery': query, 'results': results})
    else:
       
        print('home')
        return redirect('home_page') 
    
def dadaExport(request):
    if request.user.is_authenticated:  
        query = request.GET.get('q', '')
        query1 = request.GET.get('exp', '')
        file_name = "products-data.xlsx"  
        if query1 == 'search':
            print(query)
            sQuery = str("%")+query.replace(" ", "%")+str("%") 
            objs = Products.objects.raw("SELECT *  FROM `Products` WHERE `productTitle` LIKE %s ", [sQuery])
        else:
            objs=Products.objects.all()

        #export_dir = "/media/"  # Replace with the actual directory path    
        # export_file = export_dir + file_name
        data= []
        for row in objs:
            data.append({
                "productID": row.productID,
                "productTitle":row.productTitle,
                "seriesID":row.seriesID,
                "description":row.description,
                "price":row.price,
                "productImage":row.productImage,
                "searchUrl":row.searchUrl,
                "shortDescription":row.shortDescription,
                "additional1":row.additional1,
                "additional2":row.additional2,
                "additional3":row.additional3,
                "esUrl":row.esUrl,
                "pniUrl":row.pniUrl,
                "tabData":row.tabData,
                # "categoryId":row.categoryId
        })
        pd.DataFrame(data).to_excel(file_name, index=False)
    
    
        # file_obj = get_object_or_404(YourModel, id=file_id)  # Replace with your model and logic to fetch the file
        # file_path = file_obj.file.path  # Get the file's full path
        response = FileResponse(open(file_name, 'rb'))
        # response['Content-Disposition'] = f'attachment; filename="{file_obj.file.name}"'  # Sets the filename for download
        return response
        # return JsonResponse({'data':objs})
        # return render(request, 'success.html',{'data1':data})
    else:
        return redirect('home_page')


def productLoadByExtension(request):
     
    return redirect('home_page')        
         



def csvUpload(request):
    if request.user.is_authenticated:  
        if request.method == "POST": 

            if bool(request.FILES.get('csv_file', False)) == True:
                uploaded_file = request.FILES['csv_file']   
                # if not os.path.exists('product_csv/'):
                #     os.mkdir('product_csv/') 
                # print(uploaded_file.name)
                fs = FileSystemStorage()
                document_path = fs.save(uploaded_file.name, uploaded_file) 
                print(document_path)
                # document_path = default_storage.save(file.name, file)
                xl = pd.read_excel("media/"+str(document_path), "products")
                productList=[]
                productLi= {} 
                count = 0
                for i in range(0,len(xl)):  

                    productList.append(xl["productID"][i])
                    productLi[(xl["productID"][i])]=(xl["searchUrl"][i])
                    productId = str(xl["productID"][i]).strip()
                    searchUrl  = slugify(str(xl["searchUrl"][i]).strip())
                    # print(count, "productId: ", productId)

                    checkExit=Products.objects.filter(productID = productId).first() 
                    chk_url = Products.objects.filter(searchUrl = searchUrl).first() 
                    if not checkExit:  
                        if not chk_url:  
                            Products.objects.create(
                                productID = clean_excel_value(xl["productID"][i]), 
                                productTitle  = clean_excel_value(xl["productTitle"][i]), 
                                seriesID  = clean_excel_value(xl["seriesID"][i]), 
                                description = clean_excel_value(xl["description"][i]), 
                                price = clean_excel_value(xl["price"][i]).strip(), 
                                productImage = clean_excel_value(xl["productImage"][i]), 
                                searchUrl  = clean_excel_value(searchUrl), 
                                shortDescription = clean_excel_value(xl["shortDescription"][i]), 
                                additional1 = clean_excel_value(xl["additional1"][i]), 
                                additional2 = clean_excel_value(xl["additional2"][i]), 
                                additional3 = clean_excel_value(xl["additional3"][i]), 
                                esUrl = clean_excel_value(xl["esUrl"][i]), 
                                pniUrl = clean_excel_value(xl["pniUrl"][i]), 
                                tabData = clean_excel_value(xl["tabData"][i])
                                #categoryId = xl["categoryId"][i]
                            )
                        else: 
                            message = f"Duplicate URLs found.  ProductI={chk_url.productID} and sourceUrl={chk_url.searchUrl} "
                            return render(request, 'csv-upload.html', {'message': message})

                         
                    else: 
                        if checkExit.searchUrl  == searchUrl: 
                            Products.objects.filter(productID = productId).update(
                                productTitle  = clean_excel_value(xl["productTitle"][i]), 
                                seriesID  = clean_excel_value(xl["seriesID"][i]), 
                                description = clean_excel_value(xl["description"][i]), 
                                price = clean_excel_value(xl["price"][i]).strip(), 
                                productImage = clean_excel_value(xl["productImage"][i]), 
                                searchUrl  = clean_excel_value(searchUrl), 
                                shortDescription = clean_excel_value(xl["shortDescription"][i]), 
                                additional1 = clean_excel_value(xl["additional1"][i]), 
                                additional2 = clean_excel_value(xl["additional2"][i]), 
                                additional3 = clean_excel_value(xl["additional3"][i]), 
                                esUrl = clean_excel_value(xl["esUrl"][i]), 
                                pniUrl = clean_excel_value(xl["pniUrl"][i]), 
                                tabData = clean_excel_value(xl["tabData"][i]),
                                #categoryId = xl["categoryId"][i]
                            )
                        else: 
                            if not chk_url: 
                                Products.objects.filter(productID = productId).update(
                                    productTitle  = clean_excel_value(xl["productTitle"][i]), 
                                    seriesID  = clean_excel_value(xl["seriesID"][i]), 
                                    description = clean_excel_value(xl["description"][i]), 
                                    price = clean_excel_value(xl["price"][i]).strip(), 
                                    productImage = clean_excel_value(xl["productImage"][i]), 
                                    searchUrl  = clean_excel_value(searchUrl), 
                                    shortDescription = clean_excel_value(xl["shortDescription"][i]), 
                                    additional1 = clean_excel_value(xl["additional1"][i]), 
                                    additional2 = clean_excel_value(xl["additional2"][i]), 
                                    additional3 = clean_excel_value(xl["additional3"][i]), 
                                    esUrl = clean_excel_value(xl["esUrl"][i]), 
                                    pniUrl = clean_excel_value(xl["pniUrl"][i]), 
                                    tabData = clean_excel_value(xl["tabData"][i]),
                                    #categoryId = xl["categoryId"][i]
                                ) 
                            else: 
                                message = f"Duplicate URLs found.  ProductI={chk_url.productID} and sourceUrl={chk_url.searchUrl} "
                                return render(request, 'csv-upload.html', {'message': message})
                  

            
                return render(request, 'success.html',{'da':productLi,'data':productList})
        else:
            print('after post')
            # form = CSVUploadForm()
            return render(request, 'csv-upload.html') 
    
    else:
       
        print('home')
        return redirect('home_page')        
def check_identity(data):
    print('current sourceUrl check_identity:',data)
    
    # seri = SeriesItem.objects.filter(sourceUrl=data).first()
    # if seri:
    #     return seri
    cate = CategoryItem.objects.filter(sourceUrl=data).first()
    if cate:
        return cate
    pro = ProductItem.objects.filter(sourceUrl=data).first()
    if pro:
        return pro

    

        


         
    
    
    
def get_or_create_brand(current):
    print('get_or_create_brand param:',current)
    brandArr = current.strip("/").split("/")  # ['brand', 'aro']
    root_textId = 'root'
    if len(brandArr) == 2 and brandArr[0] == "brand":
        root_textId = slugify(brandArr[1])
        b_cre= Brand.objects.get_or_create(
            textId= root_textId,
            defaults={
                'title': brandArr[1], 
            }
        )
    if not CategoryItem.objects.exists():
        
        cat_obj, created = CategoryItem.objects.get_or_create(
            textId=root_textId,
            defaults={
                'title': brandArr[1],
                'url': root_textId,
                'sourceUrl': current,
                'sub_title': '',
                'parrent': 'brand',
                'type': 'brand',
                'details': '',
                'img': '',
                'status': 'y',
                'brand': brandArr[1],
            }
        )
     
    
 
    return JsonResponse(
            {
                'success': False,
                'message': 'No more URLs to process'
            },
            status=200
        ) 
             


def product_handler(currentUrl, data, previous_item):
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
        
        related_item = data.get('related_item', '')
        print('_________________________create new with url__________________________', data.get('shortDescription', '')), 
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
            additional3 = data.get('additional3', ''),
            esUrl = clean_excel_value(data.get('esUrl', '')),
            pniUrl = clean_excel_value(data.get('pniUrl', '')),
            tabData = clean_excel_value(data.get('tabData', ''))
        )
        if not related_item:
            for each_product in related_item:
                print('item.ProductId:',)
                p_textId = slugify(each_product.get('title'))
                p_url = each_product.get('sourceUrl', '')
                chk_product= ProductItem.objects.filter(sourceUrl=p_url).first()
                if not chk_product:
                    p_obj, created=ProductItem.objects.get_or_create(
                        textId=p_textId,
                        defaults={
                            'title': each_product.get('title', ''),
                            'url': p_textId,
                            'sourceUrl': each_product.get('sourceUrl', ''),
                            'brand':brand or '',
                            'img': each_product.get('img', ''),
                            'stock': each_product.get('stock', ''),
                            'status': 'n',
                            'category': 'accessories', 
                        }
                    )
        
        get_next_page(currentUrl)
    else:
        get_next_page(currentUrl)
        # return JsonResponse({'error': 'Data not found'}, status=404)
    
def category_handler(currentUrl, data):
    
    if currentUrl and hasattr(currentUrl, 'sourceUrl'):
        print('call category_handler',currentUrl.sourceUrl)
        parrent = currentUrl.textId
        brand = getattr(currentUrl, 'brand', None)
    else:
        brand = Brand.objects.filter().first()
        parrent = 'root'
        brand = brand.title

    
    for item in data:
        print(f"DEBUG: Line no: {inspect.currentframe().f_lineno} {item.get('title','')}")
         
        textId = slugify(item.get('title', ''))
        # textId= slugify(item.get('title',''))
        type = item.get('type', '')
        status = 'n' if item.get('sourceUrl') else 'y' 
        # sourceUrl = item.get('sourceUrl', '') if item.get('sourceUrl', '') else slugify(item.get('title', ''), allow_unicode=True)
        sourceUrl = item.get('sourceUrl') or f"/search/?q={quote_plus(slugify(item.get('title',''), allow_unicode=True))}"

        if parrent!='root' and type=='root' and sourceUrl=='/ask-now-form':
            continue
        

        # print(f"=====Line no: {inspect.currentframe().f_lineno}=========',{textId}")
        parrent_Item= CategoryItem.objects.filter(sourceUrl=sourceUrl).first()
        # print('==============',textId, 'parrent: ',parrent)
        if not parrent_Item:
            print('category::: ',sourceUrl ,'____',textId,'___')
            cat_obj, created = CategoryItem.objects.get_or_create(
                textId=textId,
                defaults={
                    'title': item.get('title', ''),
                    'url': textId,
                    'sourceUrl': sourceUrl,
                    'sub_title': item.get('subTitle', ''),
                    'parrent': parrent,
                    'type': item.get('type', 'category'),
                    'details': item.get('details', ''),
                    'img': item.get('img', ''),
                    'status': status,
                    'brand': brand or '',
                }
            )

            print('created category:', cat_obj.textId)
            saved_items = []
            seriseData = item.get('series')
            # category= slugify(item.get('title'))
            if seriseData: 
                for each in seriseData: 
                    each_url = each.get('sourceUrl', '')
                    each_textId= slugify(each.get('title'))
                    if each_url=='/ask-now-form':
                        continue

                    new_seriseData= CategoryItem.objects.filter(sourceUrl=each_url).first()
                    if not new_seriseData:
                        CategoryItem.objects.get_or_create(
                            textId= each_textId,
                            defaults={
                            'title': each.get('title', ''),
                            'url': each_textId,
                            'sourceUrl': each_url,
                            'sub_title': each.get('subTitle', ''),
                            'parrent':cat_obj.textId,
                            'type':each.get('type', 'series'),
                            'details': each.get('details', ''),
                            'img': each.get('img', ''),
                            'status': 'n',
                            'brand': brand or '',
                            }
                        )
            productData = item.get('products') 
            if productData: 
                for each_product in productData: 
                    p_url = each_product.get('sourceUrl', '')
                    if p_url=='/ask-now-form':
                        continue

                    p_textId = slugify(each_product.get('title'))
                    chk_product= ProductItem.objects.filter(sourceUrl=p_url).first()
                    if not chk_product:
                        p_obj, created=ProductItem.objects.get_or_create(
                            textId=p_textId,
                            defaults={
                                'title': each_product.get('title', ''),
                                'url': p_textId,
                                'sourceUrl': each_product.get('sourceUrl', ''),
                                'brand':brand or '',
                                'img': each_product.get('img', ''),
                                'stock': each_product.get('stock', ''),
                                'status': 'n',
                                'category': cat_obj.textId, 
                            }
                        )
                        saved_items.append(p_obj.textId)
                    saved_items.append(p_textId)
            update_product_csv(saved_items, cat_obj.textId) 
    # if item.get('type')=='category':
    #     sourceUrl = CategoryItem.objects.exclude(status='y').values_list('sourceUrl', flat=True).first()
    
    get_next_page(currentUrl)
        
        # print(f"Line no: {inspect.currentframe().f_lineno}", sourceUrl, '____')

        # return JsonResponse({'success': True, 'next': sourceUrl})

    # return JsonResponse({'error': 'Data not found'}, status=404)


def product_list_handler(currentUrl, data, previous_item):

    print('call product_list_handler')

    if currentUrl:
        print('currentUrl found:', currentUrl.sourceUrl)
        # print('currentUrl found:', currentUrl.type)
        # print('currentUrl found:', currentUrl.parrent)
        category = currentUrl.textId
        brand = currentUrl.brand
        serise_textId = currentUrl.textId or ''
        if currentUrl.type in ['series', 'pagination']:
            category = currentUrl.parrent
            # print('====================parrent=====================:', category)
        # print(currentUrl.type,'=====================text====================:', currentUrl.parrent, '____', currentUrl.sourceUrl)


        # up=CategoryItem.objects.filter(sourceUrl=currentUrl.sourceUrl).update( status='y')
        # print('updated category sourceUrl status:', up)
        # sourceUrl = CategoryItem.objects.exclude(status='y').values_list('sourceUrl', flat=True).first()
        saved_items = []
    
        for item in data:
            item_url= item.get('sourceUrl', '')
            textId= slugify(item.get('ProductId'))
            if item_url=='/ask-now-form':
                continue

            thisItem= ProductItem.objects.filter(sourceUrl=item_url).first()
            
            if not thisItem:
                # print('===========================452==========================', item.get('sourceUrl', ''))
                obj, created=ProductItem.objects.get_or_create(
                    textId=textId,
                    defaults={
                        'title': item.get('title', ''),
                        'url': textId,
                        'sourceUrl': item_url,
                        'brand': item.get('brand', '') or brand,
                        'img': item.get('img', ''),
                        'stock': item.get('stock', ''),
                        'status': 'n',
                        'category': category,
                        'series': serise_textId
                    }
                )
                saved_items.append(obj.textId)

                
                print('########### obj:', obj.textId)
            print('########### loop:', item.get('ProductId'))
            saved_items.append(slugify(item.get('ProductId')))
        # if saved_items:
        update_product_csv(saved_items, serise_textId) 
        update_product_csv(saved_items, category) 
    return get_next_page(currentUrl)
    
def update_product_csv(saved_items, category):
    # print('#################################',category)
    if saved_items:
        cat = CategoryItem.objects.filter(textId=category).first()

        # print('#################################',saved_items)
        

        existing_items = []
        if not cat:
            print('Category not found for textId:', category)
        else:

            if cat.product_csv:
                try:
                    existing_items = json.loads(cat.product_csv)
                except Exception:
                    existing_items = cat.product_csv.split(',')

            # merge + remove duplicates
            merged_items = list(set(existing_items + saved_items))

            cat.product_csv = json.dumps(merged_items)
            # cat.status = 'y'
            cat.save(update_fields=['product_csv'])
            # print(f'******csv data save in category {category}****:', saved_items)


def pagination_handler(data):
    # print('=====================================pagination_handler===========================================',data, data.get('sourceUrl'))
    row = CategoryItem.objects.filter(sourceUrl=data.get('sourceUrl')).first()

    if row and (row.totalPageCount is None or row.queryString in [None, '']):
        row.totalPageCount = data.get('page_count')
        row.totalListPage  = 1
        row.queryString = data.get('queryPara')
        row.save()



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
    previous_item = False
    pagination = data.get('pagination')

    clean_url = remove_last_page_param(current)
    print('clean_url', clean_url)
 
     
    # print('*********************** pagination: ', pagination)
    # print('***********************category: ', category)
    # print('***********************productList: ', productList)
    # print('***********************productData: ', productData)
    # print('*********************** current sourceUrl: ', current) 
    

    
    if not Brand.objects.exists():
        brand_obj = get_or_create_brand(clean_url)
         
    current_page = check_identity(clean_url)
    # print('++++++++++++++++++++++++++', current_page)
   
    # return JsonResponse({'error': 'currentUrl not found in database'}, status=404)
             

    returnData = None

    if category:
        returnData= category_handler(current_page, category)
    if productList:
        # print('product list found', productList)
        returnData= product_list_handler(current_page, productList, previous_item)
    if productData:
        returnData= product_handler(current_page, productData, previous_item)
   

    if pagination and isinstance(pagination, dict):
        pagination_handler(pagination)



    
    if returnData is not None:
        print('data is not None:', returnData)
        return  returnData
    else:
        print(f"Line no: {inspect.currentframe().f_lineno}",  'data not found')
        return get_next_page(current_page)
    # return JsonResponse({'success': True, 'action': 'updated', })

def get_next_page(current):
    print('694===============next page called', current)
    # print('===============textId', current.textId)
    # print('===============title', current.title)
    # print('===============sourceUrl', current.sourceUrl)
    # print('===============totalListPage', current.totalListPage)
    # print('===============totalPageCount', current.totalPageCount)
    # print('===============queryString', current.queryString)
    # print('=============== next page', build_page_url('/search/?q=ARO+PD03P-XXS-XXX', 1, 'pPgNo'))
    
    # if hasattr(currentUrl, 'type'):
    obj = CategoryItem.objects.filter(sourceUrl=current.sourceUrl).first() 
    # if obj:
        # print('707===============totalListPage', obj.totalListPage)
        # print('708===============totalPageCount', obj.totalPageCount)
        # print('709===============queryString', obj.queryString)
            
    if (
        obj
        and obj.status == 'n'
        and obj.totalPageCount is not None
        and obj.totalListPage is not None
        and obj.totalListPage > 9
        # and obj.totalPageCount > obj.totalListPage
    ):
        page_no = obj.totalListPage + 1

        new_url = build_page_url(obj.sourceUrl, page_no, obj.queryString)

        obj.totalListPage = page_no 
        obj.save(update_fields=['totalListPage'])
        print('===========================sourceUrl redirectUrl', new_url)
        return JsonResponse({'success': True, 'redirectUrl': new_url})
            
    else:
        if obj:
            obj.status = 'y'
            obj.save()
            # print('updated category sourceUrl status:', obj.sourceUrl)
        # sourceUrl = CategoryItem.objects.exclude(status='y').values_list('sourceUrl', flat=True).first()
        sourceUrl = CategoryItem.objects.exclude(status='y').exclude(sourceUrl='').values_list('sourceUrl', flat=True).first()

        if sourceUrl:
            if not sourceUrl.startswith('/'):
               
                o_bj=CategoryItem.objects.filter(
                    sourceUrl=sourceUrl
                ).update(status='y')
                print('||||||||||update status:', sourceUrl)
                sourceUrl = CategoryItem.objects.exclude(status='y').exclude(sourceUrl='').values_list('sourceUrl', flat=True).first()

            # print('next category sourceUrl found:', sourceUrl)
            return JsonResponse({'success': True,  'redirectUrl': sourceUrl})
    
    ProductItem.objects.filter(sourceUrl=current).update( status='y')

    sourceUrl = ProductItem.objects.exclude(status='y').exclude(sourceUrl='').values_list('sourceUrl', flat=True).first()
    if sourceUrl:
        # print('next product sourceUrl found:', sourceUrl)
        return JsonResponse({'success': True, 'redirectUrl': sourceUrl})
    
    return JsonResponse(
        {
            'success': False,
            'message': 'No more URLs to process'
        },
        status=200
    )  

def impoerEmployeeFromExcel(request):
    # products_file = request.FILES["products_file"]
    # rows = TextIOWrapper(products_file, encoding="utf-8", newline="")
    xl = pd.read_excel("attendance_app/employee_list.xlsx", "products")
    for i in range(0,len(xl)):  
        print()
        # Products.objects.create(
        #     branch_id = 1, employee_id = xl["Employee Id"][i],department_id = xl["Department"][i],
        #     designation_id = xl["Designation"][i], first_name = xl["First Name"][i], 
        #     last_name = xl["Last Name"][i], father_name = xl["Father Name"][i], mother_name = xl["Mother Name"][i],
        #     mobile = xl["Mobile"][i], email = xl["Email"][i], gender = xl["Gender"][i], religion = xl["Religion"][i],
        #     date_of_birth = xl["Date of Birth"][i], nationality = xl["Nationality"][i]
        # ) 
    return redirect('/dashboard/')





