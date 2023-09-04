from django.db import models

# Create your models here.

class Register(models.Model):
    name =  models.CharField(max_length=255,null=True,blank=True)
    username =  models.CharField(max_length=255,null=True,blank=True)
    email =  models.CharField(max_length=255,null=True,blank=True)
    phonenumber = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name