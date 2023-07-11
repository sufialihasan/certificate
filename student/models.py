from django.db import models


# Create your models here.
class store(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=60)
    certificate=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    gender=models.CharField(max_length=40)