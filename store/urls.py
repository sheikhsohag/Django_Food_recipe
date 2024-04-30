from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name="home"),
    path('', views.Store, name='store'),
    path('category/<slug:category_slug>/', views.Store, name='category_product'),
    path('create_menu/',views.create_recipe, name='create_menu'),
    path('update_recipe/<int:product_id>/', views.update_recipe, name='update_recipe'), 
    path('product_details/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'), 
    path('delete_recipe/<int:recipe_id>/', views.Delete_recipe, name='delete_recipe'), 
    path('search/',views.search, name='search'),
    path('Product/details/Review/<slug:category_slug>/<slug:product_slug>/', views.product_detail_review, name="product_details_reviews"),
]
