from django.db import models

# Create your models here.

class logindata(models.Model):
    email=models.EmailField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    def __str__(self):
        return self.email

class student(models.Model):
    name=models.CharField(max_length=100)
    standard=models.CharField(max_length=100)
    roll_number=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,primary_key=True)
    def __str__(self):
        return self.email

class photodata(models.Model):
    email=models.CharField(max_length=100,primary_key=True)
    photo=models.TextField(max_length=1000,default='no file')
    def __str__(self):
        return self.email

class employee(models.Model):
    name=models.CharField(max_length=100)
    ID=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,primary_key=True)
    contact=models.CharField(max_length=100)
    def __str__(self):
        return self.email

class admindata(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,primary_key=True)
    contact=models.CharField(max_length=100)
    def __str__(self):
        return self.email

class requests(models.Model):
    email=models.EmailField(max_length=100,primary_key=True)
    message=models.TextField(max_length=1000)
    name=models.TextField(max_length=100,default='no update')
    standard=models.TextField(max_length=100,default='no update')
    roll_number=models.TextField(max_length=100,default='no update')

    def __str__(self):
        return self.email

class fees(models.Model):
    email=models.EmailField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    standard = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=100)
    fees_due=models.PositiveIntegerField(default=1)
    photo = models.TextField(max_length=1000, default='no')
    def __str__(self):
        return self.email















