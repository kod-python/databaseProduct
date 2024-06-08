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
    path('cart/delete/<int:product_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('cart/edit/', views.edit_cart, name='edit_cart'),
   
   
]







