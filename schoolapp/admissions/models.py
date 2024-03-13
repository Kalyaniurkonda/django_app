from django.db import models

# Create your models here.
class student(models.Model):#create table table_name
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=200)
    age = models.IntegerField()
    mobole = models.CharField(max_length=100)