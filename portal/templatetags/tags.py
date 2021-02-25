from django import template
from .. import models
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def checkFavourite(article, user):
    try:
        status = article.check_favourite(user.person)
        print(status)
        return status
    except:
        return False

@register.filter
def checkFollows(user, person):
    try:
        models.Relationship.objects.get(from_person=user.person, to_person=person)
        return True
    except:
        return False