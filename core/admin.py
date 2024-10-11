from django.contrib import admin
from .models import Publication, Category


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
