from django.contrib import admin
from .models import Wishlist, Gift

# Customizing the admin interface for Wishlist model
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')  # Columns to display in the list view
    search_fields = ('name', 'user__username')  # Search by wishlist name and username
    list_filter = ('user',)  # Filter by user in the admin

# Customizing the admin interface for Gift model
class GiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'wishlist', 'price', 'purchased')  # Columns to display
    search_fields = ('name', 'wishlist__name')  # Search by gift name and wishlist name
    list_filter = ('wishlist', 'purchased')  # Filter by wishlist and purchased status

# Register models with the customized admin interface
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Gift, GiftAdmin)
