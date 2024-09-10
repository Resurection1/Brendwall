from django.contrib import admin

from api.models import TestModels


@admin.register(TestModels)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'price',
    )
    list_display_links = ('title',)
