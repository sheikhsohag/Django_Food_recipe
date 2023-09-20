from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'ingredients', 'instructions', 'image', 'category']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'ingredients', 'instructions','image','category',]
