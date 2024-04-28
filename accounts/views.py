from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from . models import UserProfile
from store.models import Product
from django.views.generic import ListView


# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        # print("======ok==================")
        form = RegistrationForm(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/register.html',{'form' : form})

def user_login(request):
    print("=====ok=====", request)
    if request.method == 'POST':
        print("===post ==", request)
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
        
        context =  {'profile' : user_profile, 'user_recipe':user_recipe}
        
        return render(request, 'accounts/profile.html', context)
    else:
        user_profile = User.objects.get(username=request.user.username)
        user_recipe = Product.objects.filter(author=user_profile)
        
        context =  {'profile' : user_profile, 'user_recipe':user_recipe}
        
        return render(request, 'accounts/profile.html', context)
    

def user_logout(request):
    logout(request)
    return redirect('login')


class UserProfileDetailView(ListView):
    model = UserProfile
    template_name = 'accounts/profile_copy.html'
    context_object_name = 'profile'
    
    def get_queryset(self):
        username = self.kwargs['username']
        queryset = UserProfile.objects.filter(user=username)
        print(queryset)
        return queryset