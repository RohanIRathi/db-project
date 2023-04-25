from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/register/', views.register, name='customer_register', kwargs={'mode': 'customer'}),
    path('supplier/register/', views.register, name='supplier_register', kwargs={'mode': 'supplier'}),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]