from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class Destinations(models.Model):
    
    names= models.CharField(max_length=100)
    imgs = models.ImageField(upload_to='media') 
    descs= models.TextField()
    prices = models.IntegerField()
    offers= models.BooleanField(default=False)

class Credentials(models.Model):

    questions = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)


#class UserProfile(models.Model):

   # ProfilePic = models.ImageField(upload_to='media')
 #   bio = models.CharField(max_length=30)


class UserProfileManager(BaseUserManager):
    """HELPS django work woth our custom user model"""


    def create_user(self,email,name,password=None):


      if not email:
        raise ValueError('user must have an email')

      email = self.normalize_email(email)
      user = self.model(email=email,name=name)

      user.set_password(password)
      user.save(using=self.db)
      return user


class Feed(models.Model):

    posts = models.ImageField(upload_to='media')
 



    