from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)
    return render(request, "cart.html", {"items": items, "total": total})


def checkout(request):
    return render(request, 'checkout.html')

def product_detail(request):
    return render(request, 'product_detail.html')
  
def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def coming_soon(request):   
    return render(request, 'coming_soon.html')

def error_404(request, exception):
    return render(request, '404.html')

def maintenance(request):
    return render(request, 'maintenance.html')

def sitemap(request):
    return render(request, 'sitemap.html')

def search_results(request):
    return render(request, 'search_results.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def order_history(request):
    return render(request, 'order_history.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def newsletter_subscription(request):
    return render(request, 'newsletter_subscription.html')

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failure(request):
    return render(request, 'payment_failure.html')

def product_reviews(request):
    return render(request, 'product_reviews.html')


def update_cart(request, product_id, action):
    cart = request.session.get('cart', {})

    if str(product_id) not in cart:
        return redirect('cart')

    if action == "increase":
        cart[str(product_id)] += 1
    elif action == "decrease":
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1

    request.session['cart'] = cart
    return redirect('cart')


def remove_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if item already exists
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('index')  # redirect to homepage
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

def user_profile(request):
    return render(request, 'userprofile.html')

def about_us(request):
    return render(request, 'about_us.html')

def shop2(request):
    return render(request, 'shop2.html')

def product_list(request):
    context = {
        "all_products": Product.objects.all(),
        "ordinary": Product.objects.filter(category="ordinary"),
        "exotic": Product.objects.filter(category="exotic"),
        "fertilizer": Product.objects.filter(category="fertilizer"),
        "decor": Product.objects.filter(category="decor"),
    }
    return render(request, "products.html", context)

def Blog(request):
    return render(request, 'Blog.html')