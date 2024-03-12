from django.urls import path, include
from . import views
from .views import UserProfileDetailView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:usernam>/', views.profile, name='profiles'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('profile/<str:username>', UserProfileDetailView.as_view(), name='user_profile'),
]