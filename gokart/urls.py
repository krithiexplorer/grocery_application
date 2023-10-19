from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('shop/', views.shop, name="shop"),
    path('shop-detail/', views.shopdetail, name="shopdetail"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('my-account/', views.myaccount, name="myaccount"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
]
