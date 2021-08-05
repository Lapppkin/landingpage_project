from django.contrib import admin
from .models import PriceCard, PriceTable, ProductCard

# Register your models here.
admin.site.register(ProductCard)
admin.site.register(PriceTable)
admin.site.register(PriceCard)