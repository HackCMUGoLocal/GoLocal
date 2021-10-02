from django.contrib import admin

# Register your models here.
from .models import Store
admin.site.register(Store)

from .models import Product
admin.site.register(Product)
