from django import template
# from category import models
from category.models import *
from searchApp.models import *

register = template.Library()

@register.filter('testLoader')
def my_tag(value):
    print(value)
    return value.upper()  # Example tag for uppercase conversion

@register.filter(name='navRoot')
def navRoot_load(request, data):
    navigation = CategoryItem.objects.filter(parrent=data, status='y').exclude(type='pagination').order_by('rank')

    if navigation:
        return navigation
    return None  
