from django.db import models
class Register(models.Model):
    FullName=models.CharField(primary_key=True,max_length=30)
    Email=models.CharField(max_length=30)
    Password=models.CharField(max_length=10)
    GraduationYear=models.CharField(max_length=4)
    PhoneNo=models.CharField(max_length=15)
    desig=models.CharField(max_length=15,default="user")
    def __str__(self):
        return self.Email
class Contactus(models.Model):
    Name=models.CharField(primary_key=True,max_length=30)
    Email=models.CharField(max_length=30)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=400)
    def __str__(self):
        return self.Name