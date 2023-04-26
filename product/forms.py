from django import forms

from .models import Product

class AddProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea({'rows': 5}))
    
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'category', 'price', 'qty')