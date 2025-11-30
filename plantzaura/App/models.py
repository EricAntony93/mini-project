from django.conf import settings
from django.db import models
import django.db.models.deletion
from django.contrib.auth.models import User

class BillingDetails(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        null=True,                 # TEMPORARY for migration safety
        blank=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mobile}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()  # changed from DecimalField to FloatField
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products', null=True, blank=True)

    category = models.CharField(
        max_length=20,
        choices=[
            ('ordinary', 'Ordinary Plants'),
            ('exotic', 'Exotic'),
            ('fertilizer', 'Fertilizers & Accessories'),
            ('decor', 'Decor'),
        ],
        default='ordinary'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return getattr(self.user, "username", f"UserProfile #{self.pk}")

class CartItem(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user} x {self.product} ({self.quantity})"

    def total_price(self):
        try:
            return float(self.product.price) * int(self.quantity)
        except:
            return 0.0
