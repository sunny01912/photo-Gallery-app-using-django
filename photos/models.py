from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=True)
    def __str__(self):
        return self.name

class Photo(models.Model):
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=True)

    img=models.ImageField(upload_to='photos/images',blank=False)
    description=models.TextField()


    
