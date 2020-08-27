from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, default=None)

    def _str_(self):
        return self.location

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()