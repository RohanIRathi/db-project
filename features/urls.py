from django.urls import path

from . import views

urlpatterns = [
    path('view_cart/', views.view_cart, name='view_cart'),
    path('addToCart/', views.add_to_cart, name='add_to_cart'),
    path('addBookmark/', views.bookmark, name="bookmark"),
    path('getCartCount/', views.get_cart_count, name='get_cart_count'),
    path('deleteCartItem/', views.remove_from_cart, name='remove_from_cart'),
]