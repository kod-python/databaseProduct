from django.contrib import admin
from .models import Cart
from .models import CartItem
from .models import Product

# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)