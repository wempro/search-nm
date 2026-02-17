import os
import requests
from urllib.parse import urlparse
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from bs4 import BeautifulSoup

from searchApp.models import  CategoryItem, ProductItem


def get_category_parent_tree(text_id):
    tree = []

    category = CategoryItem.objects.filter(textId=text_id).first()
    if not category:
        return tree

    # collect parents first (root → leaf)
    categories = []

    while category:
        categories.insert(0, category)
        if not category.parrent:
            break
        category = CategoryItem.objects.filter(
            textId=category.parrent
        ).first()

    # build breadcrumb
    path = "/category"
    for index, cat in enumerate(categories):
        # path += f"/{cat.textId}"
        path = f"/category/{cat.textId}"
         
        if not cat.textId == 'root':
            tree.append({
                "name": cat.textId,
                "link": None if index == len(categories) - 1 else path
            })

    return tree

def get_product_parent_tree(text_id):
    tree = []

    product = ProductItem.objects.filter(textId=text_id).first()
    if not product:
        return tree

    # category chain collect (root → leaf)
    categories = []
    category = CategoryItem.objects.filter(textId=product.category).first()

    while category:
        categories.insert(0, category)
        if not category.parrent:
            break
        category = CategoryItem.objects.filter(textId=category.parrent).first()

    # build breadcrumb with name + link
    path = "/category"
    for cat in categories:
        path = f"/category/{cat.textId}"
        tree.append({
            "name": cat.textId,
            "link": path
        })

    # last item (product) → no link
    tree.append({
        "name": product.textId,
        "link": None
    })

    return tree





def download_and_save_image(image_url, obj, field_name='img', folder='category'):
    """
    image_url   = external image link
    obj         = Django model instance (CategoryItem)
    field_name  = ImageField name (default: img)
    folder      = subfolder inside MEDIA_ROOT
    """

    if not image_url:
        return None

    try:
        response = requests.get(image_url, timeout=20)
        response.raise_for_status()

        # extract filename
        parsed = urlparse(image_url)
        filename = os.path.basename(parsed.path)

        if not filename:
            filename = 'image.jpg'

        save_path = os.path.join(folder, filename)

        # save file
        file_path = default_storage.save(
            save_path,
            ContentFile(response.content)
        )

        # update model field
        setattr(obj, field_name, file_path)
        obj.save(update_fields=[field_name])

        return file_path

    except Exception as e:
        print('Image download failed:', e)
        return None


def download_and_save_file(file_url, folder='documents'):
    if not file_url:
        return None

    try:
        response = requests.get(file_url, timeout=30)
        response.raise_for_status()

        parsed = urlparse(file_url)
        filename = os.path.basename(parsed.path)

        if not filename:
            return None

        save_path = os.path.join(folder, filename)

        file_path = default_storage.save(
            save_path,
            ContentFile(response.content)
        )

        return file_path

    except Exception as e:
        print('File download failed:', e)
        return None


 

def process_additional_html(html, brand):
    """
    HTML থেকে সব PDF link খুঁজে বের করে local path এ download করে replace করবে।
    """
    if not html:
        return html

    soup = BeautifulSoup(html, 'html.parser')

    # সব PDF <a> tag select করা
    pdf_links = soup.select('a[href$=".pdf"]')

    for pdf_tag in pdf_links:
        pdf_url = pdf_tag.get('href')
        if not pdf_url:
            continue

        # download এবং local save
        local_pdf = download_and_save_file(pdf_url, f'{brand}/pdf')
        if local_pdf:
            # replace href with local path
            pdf_tag['href'] = f'/media/{local_pdf}'

    return str(soup)

