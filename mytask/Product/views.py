from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Cart
from .models import CartItem



def index(request):
 
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


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
  
    # cart = Cart.objects.get(user=request.user)
    cart = CartItem.objects.all()
    return render(request, 'cart_detail.html', {'cart': cart})



def add_to_cart(request, id):

    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        quantity = request.POST.get('quantity', 1)
     
        cart = Cart.objects.get(user=request.user)
        cart.add(product, quantity)
        # return JsonResponse({'message': 'Product added to cart'})
        return redirect('display')
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
    # return render(request, 'add_to_cart.html')

