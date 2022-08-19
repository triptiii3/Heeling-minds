from django.db import models

# Create your models here.
class webinars(models.Model):
      name=models.CharField(max_length=50)
      email=models.CharField(max_length=50)
      phone=models.IntegerField(max_length=12)
      issue=models.CharField(max_length=50)
      mode=models.CharField(max_length=50)
      message=models.TextField(max_length=200, null=True , blank=True)

class therapies(models.Model):
      name=models.CharField(max_length=50)
      email=models.CharField(max_length=50)
      age=models.CharField(max_length=50)
      phone=models.IntegerField(max_length=12)
      gender=models.CharField(max_length=50)
      issue=models.CharField(max_length=50)
      message=models.TextField(max_length=200, null=True , blank=True)