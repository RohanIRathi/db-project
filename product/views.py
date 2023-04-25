from django.shortcuts import render
from django.contrib import messages

from .models import Product

# Create your views here.

def product_details_view(request, product_id):
	product = Product.objects.get(pk=product_id)
	if not product:
		messages.error(request, "Product Does not exist!")

	return render(request, 'product/product_details.html', {'product': product})