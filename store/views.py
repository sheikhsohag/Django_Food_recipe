from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from . models import Product
from django.http import Http404
from django.contrib.auth.decorators import login_required
from category.models import Category
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from store.models import Product
from category.models import Category


# def home(request):
#     product = Product.objects.all()
#     cat = Category.objects.all()
#     context =  {'product' : product, 'category':cat}
#     return render(request,'index.html', context)

# ==============================================================


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
        # print('baire=========')
        if form.is_valid():
            # print('valid--------------')
            slugg = form.cleaned_data['product_name']
            slugg=slugg.replace(" ","_")
            # print('-==========------dk', slugg)
            if Product.objects.filter(slug=slugg).exists():
                raise Http404("The requested slug does not exist.")
            else:
                if request.user.is_authenticated:
                    title = form.cleaned_data['product_name']
                    description = form.cleaned_data['description']
                    ingredient = form.cleaned_data['ingredients']
                    instruction = form.cleaned_data['instructions']
                    image = form.cleaned_data['image']
                    slug = slugg
                    category = form.cleaned_data['category']
                    price = form.cleaned_data['price']
                    product = Product(product_name = title, description=description, ingredients=ingredient, instructions=instruction,image=image,
                                slug=slug, category=category, author = request.user, price = price)
                    product.save()
                    return redirect('home') 
                else:
                    return redirect(request,'lonin')
    else:
        form = ProductForm()
    return render(request, 'menu_form.html', {'form' : form})



@login_required
def update_recipe(request, product_id):
    recipe = Product.objects.get(pk=product_id)
    form = ProductForm(instance=recipe)
    
    if recipe.author == request.user:
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=recipe)
            if form.is_valid():
                slugg = form.cleaned_data['product_name']
                slugg=slugg.replace(" ","_")
                title = form.cleaned_data['product_name']
                description = form.cleaned_data['description']
                ingredient = form.cleaned_data['ingredients']
                instruction = form.cleaned_data['instructions']
                image = form.cleaned_data['image']
                slug = slugg
                category = form.cleaned_data['category']
                product = Product(product_name = title, description=description, ingredients=ingredient, instructions=instruction,image=image,
                slug=slug, category=category, author = request.user)
                recipe.delete()
                product.save()
                return redirect('profile') 
        else:
            form = ProductForm(instance=recipe)
        return render(request, 'update_recipe.html', {'form': form, 'recipe': recipe})
    else:
        return redirect('home')

def product_detail(request, category_slug, product_slug):
    
    single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
    return render(request, 'product_details.html', {'recipe':single_product})

@login_required
def Delete_recipe(request, recipe_id):
    recipe = Product.objects.get(pk=recipe_id)
    if request.user == recipe.author:
        user_profile = User.objects.get(username=recipe.author.username)
        user_recipe = Product.objects.filter(author=user_profile)
        
        context =  {'profile' : user_profile, 'user_recipe':user_recipe}
        recipe.delete()
        return render(request, 'accounts/profile.html', context)
    else:
        return redirect(request, 'login')
    


def search(request):
    products=[]
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(ingredients__icontains=keyword)
            # print('==----===', products)
    return render(request, 'index.html', {'product': products})



def product_detail_review(request, category_slug, product_slug):
    
    single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
   
    return render(request, 'details_review.html', {'products':single_product})