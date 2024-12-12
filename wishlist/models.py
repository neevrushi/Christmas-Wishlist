from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlists")
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gift(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name="gifts")
    name = models.CharField(max_length=100)
    price = models.FloatField()
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.name
