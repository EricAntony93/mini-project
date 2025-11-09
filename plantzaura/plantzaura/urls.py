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
    path('about_us/',views.about_us, name='about_us'),
    path('contact/',views.contact, name='contact'),
    path('sitemap/',views.sitemap, name='sitemap'),
    path('search_results/',views.search_results, name='search_results'),
    path('newsletter_subscription/',views.newsletter_subscription, name='newsletter_subscription'),
    path('payment_success/',views.payment_success, name='payment_success'),
    path('payment_failure/',views.payment_failure, name='payment_failure'),
    path('update-cart/<int:product_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('remove-cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path('shop2/',views.shop2, name='shop2'),
    path('Blog',views.Blog, name='Blog'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)