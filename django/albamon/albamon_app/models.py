from django.db import models

# Create your models here.

class Albamon(models.Model):
    brand = models.CharField(max_length=250)
    area = models.CharField(max_length=200)
    requirement = models.CharField(max_length=500)
    wage = models.IntegerField()
    job = models.TextField()
    number = models.IntegerField()