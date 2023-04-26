from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse

from .models import Cart, Bookmark
from user.models import User, Customer
from product.models import Product

# Create your views here.

def view_cart(request):
	user = Customer.objects.get(userid=User.objects.get(email=request.user))
	cart = Cart.objects.filter(userid=user)
	
	return render(request, 'features/view_cart.html', {'cart': cart})

@csrf_exempt
def add_to_cart(request):
	if request.method == 'POST':
		user = Customer.objects.get(userid=User.objects.get(email=request.user))
		product = Product.objects.get(pk=request.POST['productid'])
		if Cart.objects.filter(userid=user).filter(productid=product).exists():
			return HttpResponse("Already in Cart", status=400)
		cart = Cart(userid=user, productid=product)
		cart.save()
		return HttpResponse("Product Added to Cart", status=200)
	return HttpResponse("Method not allowed", status=405)

def get_cart_count(request):
	cart_count = Cart.objects.filter(userid=Customer.objects.get(userid=User.objects.get(email=request.user))).count()
	request.session['cart_count'] = cart_count
	request.session.modified = True
	return HttpResponse(cart_count, status=200)

@csrf_exempt
def bookmark(request):
	if request.method == 'POST':
		user = Customer.objects.get(userid=User.objects.get(email=request.user))
		product = Product.objects.get(pk=request.POST['productid'])
		if Bookmark.objects.filter(userid=user).filter(productid=product).exists():
			return HttpResponse("Already Bookmarked", status=400)
		bookmark = Bookmark(userid=user, productid=product)
		bookmark.save()
		return HttpResponse("Product Bookmarked", status=200)
	return HttpResponse("Method not allowed", status=405)