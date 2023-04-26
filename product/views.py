from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from user.helpers import userIsSupplier
from .models import Product
from .forms import AddProductForm

# Create your views here.

@user_passes_test(userIsSupplier, redirect_field_name='home')
def add_product(request):
	if request.method == 'POST':
		form = AddProductForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Product Added!")
			return redirect('/')
		messages.error(request, "There is an error in the form")
	else:
		form = AddProductForm()
	return render(request, 'product/add_product.html', {'form': form})

def product_details_view(request, product_id):
	product = Product.objects.get(pk=product_id)
	if not product:
		messages.error(request, "Product Does not exist!")

	return render(request, 'product/product_details.html', {'product': product})