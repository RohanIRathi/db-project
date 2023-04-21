from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomerDetailsForm, SupplierDetailsForm
from .models import User, Customer
from product.models import Product
from features.models import Cart

# Create your views here.

def home(request):
	products = Product.objects.all().order_by('qty')[:20]
	cart_count = Cart.objects.filter(userid=Customer.objects.get(userid=User.objects.get(email=request.user))).count()
	return render(request, 'home/home.html', {'products': products, 'cart_count': cart_count})

def register(request, **kwargs):
	mode = kwargs.get('mode')
	if request.method == 'POST':
		u_form = CustomUserCreationForm(request.POST)
		form = CustomerDetailsForm(request.POST) if mode == 'customer' else SupplierDetailsForm(request.POST)
		if u_form.is_valid() and form.is_valid():
			user = u_form.save()
			form.save(user)
			messages.success(request, f'Account Created!')
			return redirect('/login')
		else:
			messages.error(request, f'There was an error in your form!')
	else:
		u_form = CustomUserCreationForm()
		form = CustomerDetailsForm() if mode == 'customer' else SupplierDetailsForm(request.POST)
	args = {'u_form': u_form, 'form': form}
	args.update(kwargs)

	return render(request, f'registration/register.html', args)