from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store, name='store'),
    path('category/<slug:category_slug>/', views.Store, name='category_product'),
    path('create_menu/',views.create_recipe, name='create_menu'),
    path('update_recipe/<int:product_id>/', views.update_recipe, name='update_recipe'), 
]
