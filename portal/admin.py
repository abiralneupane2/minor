from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Person)
admin.site.register(models.Article)
admin.site.register(models.Relationship)
admin.site.register(models.Favourite)
admin.site.register(models.Comment)
admin.site.register(models.Files)


