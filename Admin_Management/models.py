from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)  # Optional, since User model already has email
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(null=True,blank=True)
    profile_img = models.ImageField(default='image/default.jpg', upload_to='media')  # Add a profile image field

    def __str__(self):
        return self.user.username
    



   