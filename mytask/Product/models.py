from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name




class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_id = models.CharField(max_length=100, unique=True)
    
    
    
    
    def add(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(
            cart=self,
            product=product,
            defaults={'price': product.price, 'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return cart_item
    
 

    # def add(self, product, quantity):
    #     cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
    #     if not created:
    #         cart_item.quantity += int(quantity)
    #     else:
    #         cart_item.quantity = int(quantity)
    #     cart_item.save()
        
        
        
    def delete_item(self, product):
       
        try:
            cart_item = CartItem.objects.get(cart=self, product=product)
            cart_item.delete()
        except CartItem.DoesNotExist:
            pass 

    def clear_cart(self):
       
        CartItem.objects.filter(cart=self).delete()
    
    
    
    def update_quantity(self, product, quantity):
        try:
            cart_item = CartItem.objects.get(cart=self, product=product)
            cart_item.quantity = int(quantity)
            cart_item.save()
        except CartItem.DoesNotExist:
            pass
    
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart of {self.cart.user.username}"