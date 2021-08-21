from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    contact = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Item(models.Model):
    type = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)






class Iteam(models.Model):
   name = models.CharField(max_length=50)
   amount=models.IntegerField()
   image=models.CharField(max_length=1056)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
   def __str__(self):
     return self.name
# Create your models here.
