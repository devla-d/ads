from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
import uuid

class AccountManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')
        user = self.model(
            email = self.normalize_email(email),
            username = username
            
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,username,email,password):
        user = self.create_user(
            email= self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user


def rand_str():
	  return str(random.randint(1000000000000, 9999999999999))


class Account(AbstractBaseUser):
    email       = models.EmailField(verbose_name='email', max_length=60, unique=True )
    username    = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_advertiser = models.BooleanField(default=False)
    profile_image = models.ImageField(blank=True, null=True, default='default.jgp', upload_to='profile')
    phone = models.CharField(max_length=30, blank=True,null=True,unique=True)
    balance = models.IntegerField(default=0, blank=True,null=True)
    ip_address    = models.CharField(max_length=30,blank=True,null=True)
    package = models.IntegerField(default=1000, blank=True,null=True)
    clicks = models.IntegerField(default=0, blank=True,null=True)
    ref_code = models.CharField(max_length=50, default=rand_str(), blank=True,null=True)

    objects = AccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def __str__(self):
        return self.username