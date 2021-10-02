from django.db import models

class Bank(models.Model):
     name=models.CharField(max_length=200)
     location=models.CharField(max_length=100)
     company=models.ForeignKey()
     customer_details=models.ForeignKey()

class Company(models.Model):
     name = models.CharField(max_length=100)
     province=models.CharField(50)
     bank=models.CharField(100)
     number_of_employees=models.IntegerField()
     email=models.EmailField(),
     industrial_activites=models.CharField(max_length=500)
     registered_with=models.CharField(max_length=100)
     patnership=models.CharField(max_length=200)
     wedsite_url=models.CharField(max_length=500)

     def create_company(cls, name, loccation, registered_with,bank ):
          return cls(name,loccation,registered_with,bank)


class Organization(models.Model):
     Name =models.CharField(max_length=100)
     province=models.CharField(max_length=50)
     district = models.CharField(max_length=50)
     Bank=models.ForeignKey(Bank,on_delete=models.CASCADE,blank=False,null=False)
     company=models.ForeignKey(Company,on_delete=models.CASCADE, blank=False,null=False)
     customer=models.ForeignKey()









