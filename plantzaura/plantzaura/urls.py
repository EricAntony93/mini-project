"""
URL configuration for plantzaura project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name='index'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('product_detail/',views.product_detail, name='product_detail'),
    path('shop/',views.shop, name='shop'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path('blog_details/',views.blog_details, name='blog_details'),
    path('faq/',views.faq, name='faq'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('terms_conditions/',views.terms_conditions, name='terms_conditions'),
    path('privacy_policy/',views.privacy_policy, name='privacy_policy'),
    path('coming_soon/',views.coming_soon, name='coming_soon'),
    path('maintenance/',views.maintenance, name='maintenance'),
    path('sitemap/',views.sitemap, name='sitemap'),
    path('search_results/',views.search_results, name='search_results'),
    path('user_profile/',views.user_profile, name='user_profile'),
    path('order_history/',views.order_history, name='order_history'),
    path('wishlist/',views.wishlist, name='wishlist'),
    path('newsletter_subscription/',views.newsletter_subscription, name='newsletter_subscription'),
    path('payment_success/',views.payment_success, name='payment_success'),
    path('payment_failure/',views.payment_failure, name='payment_failure'),
    path('product_reviews/',views.product_reviews, name='product_reviews'),
]
