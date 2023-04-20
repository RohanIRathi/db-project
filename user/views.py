from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomerDetailsForm, SupplierDetailsForm
from .models import User, Customer

# Create your views here.

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