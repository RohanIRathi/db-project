from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm, CustomerDetailsForm, SupplierDetailsForm
from .models import User, Customer, Supplier
from product.models import Product
from features.models import Cart

# Create your views here.

def home(request):
	products = Product.objects.all().order_by('qty')[:20]
	return render(request, 'home/home.html', {'products': products})

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

def login(request):
	if request.method == 'POST':
		if User.objects.filter(email=request.POST['username']).exists():
			user = User.objects.get(email=request.POST['username'])
			username = user.email
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user:
				auth_login(request, user)
				if Customer.objects.filter(userid=user).exists():
					request.session['user_type'] = 'customer'
					request.session['cart_count'] = Cart.objects.filter(userid=Customer.objects.get(userid=User.objects.get(email=request.user))).count()
				elif Supplier.objects.filter(userid=user).exists():
					request.session['user_type'] = 'supplier'
				else:
					request.session['user_type'] = 'admin'
				request.session.modified = True
				print(request.session['user_type'])
				return redirect('/')
			else:
				messages.error(request, 'Incorrect Password!')
		else:
			messages.error(request, 'Email does not exist!')
	return render(request, 'registration/login.html', {'form': AuthenticationForm()})