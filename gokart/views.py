from django.shortcuts import render,redirect
from .models import Product
from .models import Cart
from .models import Wishlisted
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            messages.info(request, '* Invalid credentials,Try Again!!!')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('')
        else:
            return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, '* Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, '* Email already in use')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                auth.login(request, user)
                return redirect('')

        else:
            messages.info(request, '* Passwords dont match')
            return redirect('signup')

    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('')

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def shopdetail(request):
    products = Product.objects.all()
    return render(request, "shop-detail.html",{'products' : products})

@login_required(login_url='login')    
def checkout(request):
    return render(request, "checkout.html")       

def myaccount(request):
    return render(request, "my-account.html")    
       

@login_required(login_url='login')
def add_to_wishlist(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        user = request.user

        # Check if the product is not already in the wishlist
        if not Wishlisted.objects.filter(user=user, product_id=product_id).exists():
            Wishlisted.objects.create(user=user, product_id=product_id)

    # Redirect to the view_wishlist view
    return redirect('view_wishlist')

@login_required(login_url='login')
def view_wishlist(request):
    user = request.user
    wishlist_items = Wishlisted.objects.filter(user=user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required(login_url='login')
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        user = request.user

        # Check if the product is not already in the wishlist
        if not Cart.objects.filter(user=user, product_id=product_id).exists():
            Cart.objects.create(user=user, product_id=product_id)

    # Redirect to the view_wishlist view
    return redirect('view_cart')

@login_required(login_url='login')
def view_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    return render(request, 'cart.html', {'cart_items': cart_items})

def gallery(request):
    gallery = Product.objects.all()
    return render(request, "gallery.html", {'gallery':gallery})    

def contact(request):
    return render(request, "contact-us.html")
