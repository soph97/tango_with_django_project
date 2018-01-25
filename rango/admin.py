from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
