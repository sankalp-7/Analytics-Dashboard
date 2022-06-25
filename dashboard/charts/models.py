from operator import mod
from django.db import models

# Create your models here.
class db(models.Model):
    _id=models.AutoField(primary_key=True)
    end_year=models.CharField(max_length=10)
    intensity=models.IntegerField()
    sector=models.CharField(max_length=100)
    topic=models.CharField(max_length=1000)
    insight=models.CharField(max_length=1000)
    url=models.CharField(max_length=10000)
    region=models.CharField(max_length=100)
    start_year=models.CharField(max_length=10)
    impact=models.CharField(max_length=100)
    added=models.CharField(max_length=1000)
    published=models.CharField(max_length=1000)
    country=models.CharField(max_length=1000)
    relevance=models.IntegerField()
    pestle=models.CharField(max_length=100)
    source=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    hood=models.IntegerField()
