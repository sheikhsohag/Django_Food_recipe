from django.shortcuts import render
from store.models import Product
from category.models import Category


def home(request):
    product = Product.objects.all()
    cat = Category.objects.all()
    context =  {'product' : product, 'category':cat}
    return render(request,'index.html', context)

