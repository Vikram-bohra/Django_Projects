from django.db import models

# Create your models here.

class NAV_Details(models.Model):
    code = models.IntegerField()
    isin = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    nav = models.FloatField(max_length=20)
    date = models.CharField(max_length=30)
    usr = models.CharField(max_length=20,blank=True,null=True)