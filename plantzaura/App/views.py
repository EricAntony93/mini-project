from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem,Product,BillingDetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib import messages
from .models import Product,UserProfile
from django.core.mail import send_mail, BadHeaderError
from decimal import Decimal
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .forms import BillingDetailsForm
from django.db import transaction, OperationalError
import logging
from .forms import BillingDetailsForm


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    # Attach grand_total dynamically to each CartItem object
    for item in cart_items:
        item.grand_total = float(item.product.price) * float(item.quantity)

    total = sum(item.grand_total for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def index(request):
    products = Product.objects.all()
    ordinary_products = Product.objects.filter(category="ordinary")
    exotic_products = Product.objects.filter(category="exotic")
    fertilizer_products = Product.objects.filter(category="fertilizer")
    decor_products = Product.objects.filter(category="decor")

    return render(request, "index.html", {
        "products": products,
        "ordinary_products": ordinary_products,
        "exotic_products": exotic_products,
        "fertilizer_products": fertilizer_products,
        "decor_products": decor_products,
    })

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        item.grand_total = float(item.product.price) * float(item.quantity)

    subtotal = sum(item.grand_total for item in cart_items)
    shipping = 50.0
    grand_total = subtotal + shipping

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'grand_total': grand_total,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {"product": product})

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')


def sitemap(request):
    return render(request, 'sitemap.html')

def search_results(request):
    return render(request, 'search_results.html')

def user_profile(request):
    return render(request, 'userprofile.html')

def newsletter_subscription(request):
    return render(request, 'newsletter_subscription.html')

@login_required
def update_cart(request, product_id, action):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)

    if action == "increase":
        cart_item.quantity += 1
    elif action == "decrease" and cart_item.quantity > 1:
        cart_item.quantity -= 1

    cart_item.save()
    return redirect('cart')

@login_required
def remove_cart(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    cart_item.delete()
    return redirect('cart')

@login_required
def add_cart(request, product_id):
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

User = get_user_model()

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        # No email check in the oldest version
        # No try-except

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name,
        )

        # No user profile creation here in the oldest version

        messages.success(request, "Account created successfully!")
        return redirect("login")

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

@login_required
def payment(request):
    cart_items = CartItem.objects.filter(user=request.user)

    # SUM all item totals instead of creating a set
    grand_total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        method = request.POST.get("payment_method")
        return redirect('payment_success')

    return render(request, "payment.html", {"total_amount": grand_total + 50.0})  # including shipping



@login_required
def payment_success(request):
    # cart and totals (you had similar logic)
    cart_items = CartItem.objects.filter(user=request.user)
    grand_total = sum(item.product.price * item.quantity for item in cart_items)

    # Billing form prefill logic: prefer saved BillingDetails, otherwise use user profile
    instance = BillingDetails.objects.filter(user=request.user).order_by('-id').first()
    if instance:
        form = BillingDetailsForm(instance=instance)
    else:
        form = BillingDetailsForm(initial={
            "first_name": request.user.first_name or "",
            "last_name":  request.user.last_name or "",
            "email":      request.user.email or "",
        })

    return render(request, "success.html", {
        "total_amount": grand_total,
        "cart_items": cart_items,
        "form": form,
    })


@login_required
def save_billing(request):
    if request.method != "POST":
        return redirect('billing_details')

    # Load existing instance if exists (so update instead of create)
    instance = BillingDetails.objects.filter(user=request.user).first()

    form = BillingDetailsForm(request.POST, instance=instance)

    if form.is_valid():
        billing = form.save(commit=False)
        billing.user = request.user
        billing.save()

        # Cart items & totals
        cart_items = CartItem.objects.filter(user=request.user)
        subtotal = sum(float(item.total_price()) for item in cart_items)
        shipping = 50.0
        grand_total = round(subtotal + shipping, 2)

        subtotal = round(subtotal, 2)

        # Render HTML email
        message = render_to_string("email_receipt.html", {
            "billing": billing,
            "items": cart_items,
            "subtotal": subtotal,
            "shipping": shipping,
            "grand_total": grand_total,
        })

        # Send email (set fail_silently=False for debugging)
        send_mail(
            subject="PlantzAura - Order Receipt",
            message="",
            html_message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[billing.email],
            fail_silently=False,
        )

        return redirect('billing_success')

    # If invalid, show form again
    return render(request, "billing_details.html", {"form": form})


@login_required
def billing_success(request):
    return render(request, "billing_success.html")

@login_required
def billing_details(request):
    instance = BillingDetails.objects.filter(user=request.user).order_by('-id').first()
    if instance:
        form = BillingDetailsForm(instance=instance)
    else:
        initial = {
            "first_name": request.user.first_name or "",
            "last_name":  request.user.last_name or "",
            "email":      request.user.email or "",
        }
        form = BillingDetailsForm(initial=initial)
    return render(request, "billing_details.html", {"form": form})

