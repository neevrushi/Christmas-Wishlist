from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_list, name='wishlist_list'),
    path('create/', views.create_wishlist, name='create_wishlist'),
    path('<int:pk>/', views.manage_wishlist, name='manage_wishlist'),
    path('wishlist/<int:wishlist_id>/not-purchased/', views.not_purchased_gifts, name='not_purchased_gifts'),


]
