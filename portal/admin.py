from django.contrib import admin
from . import models
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user_type",)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Article)
admin.site.register(models.Relationship)
admin.site.register(models.Favourite)
admin.site.register(models.Comment)
admin.site.register(models.Files)





