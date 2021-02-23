from django import template
from .. import models

register = template.Library()

@register.filter
def checkFavourite(article, user):

    status = article.check_favourite(user.person)
    print(status)
    return status

