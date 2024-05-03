from django.contrib import admin
from .models import About, Food, Category


# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name', 'description', 'price')


admin.site.register(Food, FoodAdmin)
admin.site.register(Category)
admin.site.register(About)