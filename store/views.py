from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from . models import Product
from django.http import Http404
from django.contrib.auth.decorators import login_required
from category.models import Category


def Store(request, category_slug = None):
    product=None
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        product = Product.objects.filter(category=category)
    else:
        product = Product.objects.all()
    cat = Category.objects.all()
    context =  {'product' : product, 'category':cat}
    return render(request,'index.html', context)



@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            slugg = form.cleaned_data['slug']
            if Product.objects.filter(slug=slugg).exists():
                raise Http404("The requested slug does not exist.")
            else:
                if request.user.is_authenticated:
                    form.save()
                    return redirect('home') 
                else:
                    return redirect(request,'lonin')
    else:
        form = ProductForm()
    return render(request, 'menu_form.html', {'form' : form})



@login_required
def update_recipe(request, product_id):
    recipe = get_object_or_404(Product, id=product_id)
    if recipe.author == request.user:
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=recipe)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = ProductForm(instance=recipe)
        return render(request, 'update_recipe.html', {'form': form, 'recipe': recipe})
    else:
        return redirect('home')

# def product_detail(request, category_slug=None, product_slug=None):
    
#     single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
#     print('================',single_product)
       
#     return render(request, 'product_details.html', {'product':single_product})