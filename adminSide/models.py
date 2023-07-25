from django.db import models
# import json

# Create your models here.
# class Register(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=254)
#     password = models.CharField(max_length=50)


# class Image(models.Model):
#     product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images')

class Products(models.Model):
    name = models.CharField(max_length=255, default="")
    desc = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=255, default="")
    # imgs = models.ForeignKey(Image, related_name='images', on_delete=models.CASCADE)
    # imgs = models.ForeignKey(Image, default="", related_name='products', on_delete=models.CASCADE)


    # img = models.ImageField(upload_to='images', default="")
    # img = models.TextField(default="")  # Store the JSON representation of the images

    # def save(self, *args, **kwargs):
    #     self.img = json.dumps(self.img)  # Convert the list of images to JSON
    #     super().save(*args, **kwargs)


    # def __str__(self):
    #     return str(self.name)
    
class Image(models.Model):
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')