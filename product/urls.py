from django.urls import path

from . import views

# URLs for products

urlpatterns = [
    path('viewProduct/<int:product_id>', views.product_details_view, name="product_details"),
]