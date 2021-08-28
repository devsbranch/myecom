from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Iteam(models.Model):
   name = models.CharField(max_length=50)
   amount=models.IntegerField()
   image=models.CharField(max_length=1056)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
     return self.name
# Create your models here.
