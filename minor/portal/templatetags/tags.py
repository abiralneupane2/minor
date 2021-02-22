from django import template
from .. import models

register = template.Library()

@register.filter
def checkFavourite(article, user):
    print('check')
    status = article.check_favourite(user.person)
    return status

def cut(value, arg):
    """Removes all values of arg from the given string"""
    print('works')
    return value.replace(arg, '')