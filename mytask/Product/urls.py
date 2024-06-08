from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('display', views.display, name="display"),
   
]







