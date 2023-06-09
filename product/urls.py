from django.urls import path

from . import views

# URLs for products

urlpatterns = [
    path('addProduct/', views.add_product, name='add_product'),
    path('viewProduct/<int:product_id>', views.product_details_view, name="product_details"),
]