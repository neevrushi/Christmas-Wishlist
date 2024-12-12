from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist, Gift
from .forms import WishlistForm, GiftForm

@login_required
def wishlist_list(request):
    wishlists = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist_list.html', {'wishlists': wishlists})

@login_required
def create_wishlist(request):
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.user = request.user
            wishlist.save()
            return redirect('wishlist_list')
    else:
        form = WishlistForm()
    return render(request, 'wishlist_form.html', {'form': form})

@login_required
def manage_wishlist(request, pk):
    wishlist = Wishlist.objects.get(pk=pk, user=request.user)
    gifts = wishlist.gifts.all()
    return render(request, 'wishlist_manage.html', {'wishlist': wishlist, 'gifts': gifts})

from django.shortcuts import render, get_object_or_404
from .models import Wishlist, Gift

def not_purchased_gifts(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, id=wishlist_id)
    gifts = wishlist.gifts.filter(purchased=False)  # Filter gifts that are not purchased
    return render(request, 'wishlist/not_purchased_gifts.html', {'wishlist': wishlist, 'gifts': gifts})
