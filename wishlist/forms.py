from django import forms
from .models import Wishlist, Gift

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['name']

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'price', 'purchased']
