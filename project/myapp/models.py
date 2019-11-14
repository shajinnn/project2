from django.db import models

# Create your models here.

class Employee(models.Model):
    name   = models.CharField(max_length=25)
    age    = models.IntegerField()
    salary = models.IntegerField()

class Developer(models.Model):
    project     = models.CharField(max_length=50)
    fk_employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

class Login(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

class registr(models.Model):
    firstname  = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    dob        = models.DateField()
    gender     = models.CharField(max_length=30)
    fk_login   = models.ForeignKey(Login,on_delete=models.CASCADE)

class upload(models.Model):
    image = models.FileField(upload_to='image/')
    fk_login = models.ForeignKey(Login,on_delete=models.CASCADE)
