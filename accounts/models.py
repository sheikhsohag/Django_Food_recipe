from django.db import models
from django.contrib.auth.models import User
# Create your models her



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    about = models.TextField(max_length=500)
    contact = models.IntegerField(max_length=14)

    def __str__(self):
        return self.user.username