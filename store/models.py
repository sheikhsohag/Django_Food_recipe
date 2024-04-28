from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=3)

    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.TextField(max_length=500,blank=True)
    instructions = models.TextField(max_length=500,blank=True)
    image = models.ImageField(upload_to='photos/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1, related_name='user_data')
    
    
    def __str__(self):
        return self.product_name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.TextField(max_length=500)
    rating = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.id)