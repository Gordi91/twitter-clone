from django.contrib import admin

from twitter import models


@admin.register(models.Tweet)
class PersonAdmin(admin.ModelAdmin):
    pass
