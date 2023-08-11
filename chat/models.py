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


#realthionships models

# 1 to 1
class Femele(models.Model):
  name_f = models.CharField(max_length=100,null=True)
  def __str__(self):
    return self.name_f  

class Male(models.Model):
  name_m = models.CharField(max_length=100,null=True)
  girl= models.OneToOneField(Femele, on_delete=models.CASCADE)
  def __str__(self):
    return self.name_m
    


#  1 to meny
class Product(models.Model):
  name_m = models.CharField(max_length=100,null=True)
  def __str__(self):
    return self.name_m
    

class User(models.Model):
  name_f = models.CharField(max_length=100,null=True)
  products= models.ForeignKey(Product,on_delete=models.CASCADE)
  def __str__(self):
    return self.name_f  




# meny to meny




class Vedio(models.Model):
  title = models.CharField(max_length=100,null=True)
  def __str__(self):
    return self.title
    

class Client(models.Model):
  name_f = models.CharField(max_length=100,null=True)
  watch=models.ManyToManyField(Vedio,null=True)

  def __str__(self):
    return self.name_f  

