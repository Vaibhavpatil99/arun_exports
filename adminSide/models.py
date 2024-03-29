from django.db import models
from django.contrib.auth.models import User
# import json

# Create your models here.
# class Register(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=254)
#     password = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forgot_password_token = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username

class Specification(models.Model):
    header = models.CharField(max_length=255)
    description = models.TextField()

class Products(models.Model):
    name = models.CharField(max_length=255, default="")
    desc = models.TextField(blank=True, null=True)
    product_code = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=255, default="")
    subcategory = models.CharField(max_length=255, default="")
    specifications = models.ManyToManyField(Specification)

    
class Image(models.Model):
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')


class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_no = models.CharField(max_length=20)
    message = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.name