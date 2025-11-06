from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

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

def blog(request):
    return render(request, 'blog.html')
def blog_details(request):
    return render(request, 'blog_details.html')

def faq(request):
    return render(request, 'faq.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def coming_soon(request):   
    return render(request, 'coming_soon.html')

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')

def error_403(request, exception):
    return render(request, '403.html')

def error_400(request, exception):
    return render(request, '400.html')

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