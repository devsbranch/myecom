from django.db import models

class UserRegistration(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=50)



