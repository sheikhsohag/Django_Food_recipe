from django.shortcuts import render
from . models import Category

# Create your views here.

def category(request):
    model = Category.objects.all()
    print(model)
    return render(request, 'base.html', {'model' : model})
