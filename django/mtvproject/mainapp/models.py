from django.db import models

# Create your models here.
class Blog(models.Model) :
    title = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    body = models.TextField()

class Team(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField(default=0)
    major= models.CharField(max_length=100)
    residence= models.CharField(max_length=100)
    bd= models.CharField(max_length=100)
    MBTI= models.CharField(max_length=100)
    INTRO=models.CharField(max_length=300)