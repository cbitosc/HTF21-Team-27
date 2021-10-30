from django.db import models

# Create your models here.
# class ComplaintDetails(models.Model):
    


    
    # date_time = models.DateTimeField()
    # place = models.CharField(max_length=50)
    # desc = models.TextField()

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    roll_number = models.IntegerField()
    branch = models.CharField(max_length=10)
    mail = models.EmailField(max_length=256)
    password = models.CharField(max_length=16)

class Complaint(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    place = models.CharField(max_length=50)
    desc = models.TextField()

class AdminLogin(models.Model):
    emailid = models.EmailField(max_length=256)
    password = models.CharField(max_length=16)
    name = models.CharField(max_length=20)
