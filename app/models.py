from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    designation=models.CharField(max_length=50,choices=(
        ('it','it'),
        ('se','se'),
        ('ml','ml')
    ))
    
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name=models.CharField(max_length=50)
    mob_number=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    Company=models.ForeignKey(Company,on_delete=models.CASCADE)