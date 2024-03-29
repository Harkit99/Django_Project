from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import mask_hash

# Create your models here. It works on ORM(object relational mapping)
class Details(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=75)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    image = models.ImageField(upload_to='image/')
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def details(self):
        return self.summary[:50]+'...'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time']

class Register(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=25)
    email=models.EmailField(max_length=75)
    city=models.CharField(max_length=30)
    createpass=models.CharField(max_length=50)
