from django.db import models

# Create your models here.

allSize = (
    ('S', 'Small'),
    ('L', 'Large')
)

class extraSub(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()

class Subs(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.IntegerField()
    extra = models.ManyToManyField(extraSub, blank=True)

class Pizza(models.Model):
    style = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.IntegerField()
    topping = models.CharField(max_length=64)

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()

class dinnerPlatters(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    size = models.CharField(max_length=64)
