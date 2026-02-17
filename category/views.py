from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category
from searchApp.models import Products, CategoryItem, MetaData
from searchApp.utils import get_category_parent_tree, download_and_save_image
# from course.forms import ContactForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
# Create your views here.


def category(request, url):
    # query = request.GET.get('q', '')
    # print(query) 
    print('nur Category URL:', url) 
    category = Category.objects.get(categoryUrl=url)
    # category = get_object_or_404(CategoryItem, textId=url)

    
    print('nur Category URL:', url) 
    # while cate.parrentCategory !='root':
    #     categoryTree = Category.objects.get(textId=cate.parrentCategory)
    #     print()
  
    
    breadcrumbTree = category.breadcrumbTitle.split("/")
    # print(arr)
    breadcrumbText=[] 
    link = ""
    for item in breadcrumbTree:   
        title = item.replace('-', ' ')
        link = '/'+ item; 
        
        place_json = {}
        place_json["link"] = link
        place_json["title"] = title 

        breadcrumbText.append(place_json)  

    # 2️⃣ CSV string কে list এ convert করুন
    if category.productCsv:
        product_ids = [pid.strip() for pid in category.productCsv.split(',')]  
        # strip() removes whitespace if any
    else:
        product_ids = []

    # 3️⃣ ORM filter
    items = Products.objects.filter(productID__in=product_ids)
    print('nur Product product_ids:', product_ids)
    print('nur Product IDs:', items)



    # items = Products.objects.filter(categoryId=url)
    # for data in items: 
        # print(data.parrentCategory) 
        # print(data) 

    # print('nur Category',cate)
    # print('nur Product: ',items.query)
    return render(request, 'product_list.html', {'category':category ,'items':items, 'breadcrumb':breadcrumbText}) 
 


 
def all_categorries(request,url=None):
    # items = CategoryItem.objects.filter(status='y', type='category', product_csv__isnull=False)
    items = CategoryItem.objects.filter(status='y')

    
    print('All Categories Items:', items)
    meta_data = MetaData.objects.filter(textId='category').first()
    if not meta_data:
        tree= [{"name": "Show all categpries", "link": None}]
         

        meta_data, created = MetaData.objects.get_or_create(
            textId='category',
            defaults={
                'seoTitle': 'All Categories',
                'metaDescription': 'Browse all categories available on our platform.',
                'canonicalUrl': 'category',
                'breadcrumbTree': json.dumps(tree),
                'status': 'y',
            }
        )
    breadcrumb_tree = []
    if meta_data.breadcrumbTree:
        breadcrumb_tree = json.loads(meta_data.breadcrumbTree)
     

    
    if items:
    # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(items, 10)   
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
    
    
    return render(request, 'category-list.html', {'items':items, 'breadcrumb':breadcrumb_tree, 'meta_data':meta_data})

 
def category_item(request, url):
    # query = request.GET.get('q', '')
    # print(query) 
    print('nur Category URL:', url) 
    category = CategoryItem.objects.filter(textId=url).first()
    category_list = []
    
    # category = get_object_or_404(CategoryItem, textId=url)
    # print('==============================:',category.title)
    # print('======product_csv =====:',category.product_csv)
    if not category:
        return render(request, '404.html') 
        # raise Http404("Category not found")
        # return redirect('home_page')  # or any other appropriate action
    else:
        meta_data = MetaData.objects.filter(textId=category.textId).first()
        if not meta_data:
            seo_title = f"{category.title} | {category.brand}" if category.brand else category.title
            tree= get_category_parent_tree(category.textId)
            print('#### Category Tree:', tree)
            meta_description = category.sub_title if category.sub_title else category.details
            
            
            if not meta_description:
                meta_description = category.title

            meta_data, created = MetaData.objects.get_or_create(
                textId=category.textId,
                defaults={
                    'seoTitle': seo_title,
                    'metaDescription': meta_description.strip()[:150],
                    'canonicalUrl': category.textId,
                    'breadcrumbTree': json.dumps(tree),
                    'status': 'y',
                }
            )
        breadcrumb_tree = []
        if meta_data.breadcrumbTree:
            breadcrumb_tree = json.loads(meta_data.breadcrumbTree)
                        
                     
        if category.product_csv:
            try:
                # ✅ JSON array string হলে
                product_ids = json.loads(category.product_csv)

                # ensure clean strings
                product_ids = [str(pid).strip() for pid in product_ids]

            except (json.JSONDecodeError, TypeError):
                # 🔁 পুরনো comma-separated string হলে
                product_ids = [
                    pid.strip()
                    for pid in category.product_csv.split(',')
                    if pid.strip()
                ]
        else:
            product_ids = []
        category_list = CategoryItem.objects.filter(parrent=category.textId)

        # 3️⃣ ORM filter
        items = Products.objects.filter(productID__in=product_ids)
 
    
        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(items, 10)   
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        return render(request, 'product_list.html', {'items':items, 'category_list':category_list, 'meta_data':meta_data, 'breadcrumb':breadcrumb_tree}) 