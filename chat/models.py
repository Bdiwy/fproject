from django.db import models

# Create your models here.


class feature(models.Model):
  name = models.CharField(max_length=100)
  detiels = models.CharField(max_length=500)

class other(models.Model):
  name = models.CharField(max_length=100)
  detiels = models.CharField(max_length=500)

class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  comment = models.TextField()







    