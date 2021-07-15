from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_superuser(self,email,user_name, first_name,password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError (
                'Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'SuperUser must be assigned to is_superuser=True')
        
        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self,email,user_name, first_name,password, **other_fields):
        if not email:
            raise ValueError(_('You must an email address'))
        
        email = self.normalize_email(email)
        user= self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)