from django import template

register = template.Library()

@register.filter('nurTest')
def my_tag(value):
    return value.lower()  # Example tag for uppercase conversion

# @register.filter
# def my_filter(value):
#     return value * 2  # Example filter for doubling a value
