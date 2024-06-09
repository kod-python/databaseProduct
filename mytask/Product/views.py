from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Cart
from .models import CartItem
from django.contrib import messages




def index(request):
 
    products = Product.objects.all()
    
    # cart = Cart.objects.get(user=request.user)
    cart = Cart.objects.get(user=request.user)
    total_items = cart.item_count()

    return render(request, 'index.html', {'products': products, 'total_item':total_items})




def cart_font(request):
    
    return render(request, 'cart_font.html')





def display(request):
    
    return render(request, 'display.html')


def cart_add(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.add(product, quantity)
        return redirect('cart_detail')
    return render(request, 'product_detail.html', {'product': product})





def cart_detail(request):
  
    cart = get_object_or_404(Cart, user=request.user)
    
    cart_items = CartItem.objects.filter(cart=cart)
    
    
    cart_details = []
    total_price = 0
    for item in cart_items:
        item_total = item.price * item.quantity
        total_price += item_total
        cart_details.append({
            'product': item.product,
            'price': item.price,
            'quantity': item.quantity,
            'item_total': item_total,
           
        })
    
    
    
    
    # total_price = sum(item.price *  item.quantity for item in cart_items)
    # cart = CartItem.objects.all()
    return render(request, 'cart_detail.html', {'cart_details':cart_details, 'cart': cart, 'total_price':total_price})







def add_to_cart(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        quantity = int(request.POST.get('quantity', 1))
        
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.add(product, quantity)
        
        messages.success(request, "Product added to cart successfully")
        return redirect('display')





# def add_to_cart(request, id):

#     if request.method == 'POST':
#         product = get_object_or_404(Product, id=id)
#         quantity = request.POST.get('quantity', 1)
#         # cart, created = Cart.objects.get_or_create(user=request.user)
#         cart.add(product, quantity)
#         cart = Cart.objects.get(user=request.user)
#         # cart.add(product, quantity)
#         # return JsonResponse({'message': 'Product added to cart'})
#         return redirect('display')
#         # messages.SUCCESS(request, "product added to cart succesfully")
#     return JsonResponse({'error': 'Invalid request'}, status=400)
    
    # return render(request, 'add_to_cart.html')




def delete_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart.delete_item(product)
    return redirect('cart_detail')




def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.clear_cart()
    return redirect('cart_detail')





def edit_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)

    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        cart_item.quantity = int(quantity)
        cart_item.save()
        return redirect('cart_detail')

    context = {
        'cart_item': cart_item,
    }
    return render(request, 'cart/edit_cart.html')