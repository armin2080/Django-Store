from django.contrib import admin
from .models import products,subcategories,categories
# Register your models here.
admin.site.register(products)
admin.site.register(subcategories)
admin.site.register(categories)
