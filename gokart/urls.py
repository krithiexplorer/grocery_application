from django.urls import path
from .views import home,login,signup,about,shop,shopdetail,checkout,myaccount,add_to_wishlist,gallery,contact,view_wishlist,add_to_cart,view_cart

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('shop/', shop, name="shop"),
    path('shop-detail/',shopdetail, name="shopdetail"),
    path('add_to_cart/', add_to_cart, name="add_to_cart"),
    path('view_cart/', view_cart, name="view_cart"),
    path('checkout/', checkout, name="checkout"),
    path('my-account/', myaccount, name="myaccount"),
    path('add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('view_wishlist/', view_wishlist, name='view_wishlist'),
    path('gallery/', gallery, name="gallery"),
    path('contact/', contact, name="contact"),
]
