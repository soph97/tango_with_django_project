from django.contrib import admin
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


# Register your models here.

admin.site.register(Page)



class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
