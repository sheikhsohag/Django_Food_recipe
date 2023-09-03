from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from . models import UserProfile
from store.models import Product


# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/register.html',{'form' : form})

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')
    return render(request, 'accounts/signin.html')


def profile(request, usernam=None):
    
    if usernam:
        user_profile = User.objects.get(username=usernam)
        user_recipe = Product.objects.filter(author=user_profile)
        
        print('=====',user_profile.first_name)
        print(user_recipe)
        
        context =  {'profile' : user_profile, 'user_recipe':user_recipe}
        
        return render(request, 'accounts/dashboard.html', context)
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return render(request, 'accounts/signin.html')