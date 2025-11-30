from django.contrib import admin
from .models import Product, CartItem, BillingDetails

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(BillingDetails)
