from django.db import models
import random

from accounts.models import Account

def rand_str():
	  return str(random.randint(1000000000000, 9999999999999))




class Advert(models.Model):
    CONDITION = [
        ("new", "new"),
        ("old", "old")
    ]
    DAYS = [
        ('3', 3),
        ('7', 7),
        ('10', 10)
    ]
    title = models.CharField(max_length=100)
    cover_photos = models.ImageField(upload_to="cover_photos", blank=True,null=True)
    cover_photos_2 = models.ImageField(upload_to="cover_photos", blank=True,null=True)
    cover_photos_3 = models.ImageField(upload_to="cover_photos", blank=True,null=True)
    condition = models.CharField(max_length=20,choices=CONDITION)
    price = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    num_of_days = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    days = models.CharField(max_length=20,choices=DAYS)
    description = models.TextField()
    date  = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    delete_date  = models.DateTimeField(blank=True,null=True)
    brand_name = models.CharField(max_length=50)
    author = models.ForeignKey(Account, on_delete=models.CASCADE,blank=True,null=True)
    active = models.BooleanField(default=False)
    clicks = models.IntegerField(default=0,blank=True,null=True)
    ref_code = models.CharField(max_length=50, default=rand_str(), blank=True,null=True)


    class Meta:
        ordering = ['-date']



    def __str__(self):
        return self.title

    def my_clicks(self):
        total = 0
        for p in self.objects.filter(author=self.author):
            total  += p.clicks
            return total



class Withdraw(models.Model):
    amount = models.IntegerField()
    acc_num = models.CharField(max_length=50)
    acc_name = models.CharField(max_length=50)
    bank = models.CharField(max_length=50)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,blank=True,null=True)
    date  = models.DateTimeField(auto_now_add = True,blank=True,null=True)

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.user.username


