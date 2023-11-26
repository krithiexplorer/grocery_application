from django.urls import path
from .views import home,about,shop,shopdetail,cart,checkout,myaccount,wishlist,gallery,contact

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('about/', about.as_view(), name="about"),
    path('shop/', shop.as_view(), name="shop"),
    path('shop-detail/',shopdetail.as_view(), name="shopdetail"),
    path('cart/', cart.as_view(), name="cart"),
    path('checkout/', checkout.as_view(), name="checkout"),
    path('my-account/', myaccount.as_view(), name="myaccount"),
    path('wishlist/', wishlist.as_view(), name="wishlist"),
    path('gallery/', gallery.as_view(), name="gallery"),
    path('contact/', contact.as_view(), name="contact"),
]
