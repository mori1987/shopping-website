from django.contrib import admin
from .models import Product,Cart,CartItems,Order,OrderItem

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Order)
admin.site.register(OrderItem)


