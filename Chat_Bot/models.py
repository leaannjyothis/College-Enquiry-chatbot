from django.db import models
from django.contrib.auth.models import User
from .models import*

# Create your models here.
class registration(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    adno=models.CharField(max_length=200,null=True)
    department=(('1','CSE'),('2','ECE'),('3','CE'),('4','EEE'),('5','ME'),('6','AIML'),('7','M.Tech'),('8','MCA'))
    dep=models.CharField(max_length=100,choices=department,default='1')
    gender=(('M','Male'),('F','Female'),('O','Others'))
    gen=models.CharField(max_length=10,choices=gender,default='f')

class Chatbot(models.Model):
    send=models.CharField(max_length=200,null=True)
    receive=models.CharField(max_length=200,null=True)
    receive1=models.CharField(max_length=200,null=True) 
    receive2=models.CharField(max_length=200,null=True)


class Attendence(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      Name=models.CharField(max_length=200,null=True)
      Semester=models.CharField(max_length=250)
      Register_Number=models.CharField(max_length=200)
      Department=models.CharField(max_length=200)
      From=models.DateField()
      To=models.DateField()
      ta=models.CharField(max_length=250)

class Fee_Payment(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      Name=models.CharField(max_length=200,null=True)
      Semester=models.CharField(max_length=200)
      Register_Number=models.CharField(max_length=200)
      Department=models.CharField(max_length=200)
      Course_Fee=models.CharField(max_length=200)
      Paid=models.CharField(max_length=200)
      Due=models.CharField(max_length=200)
      Last_Date=models.DateField(max_length=200)

class Events(models.Model):
      Event=models.CharField(max_length=200)
      Date=models.DateField(max_length=200)
      Description=models.CharField(max_length=200)      

          
class Faculty(models.Model):
     
    name=models.CharField(max_length=100,null=True,blank=True)
    gender_choices=(
        ('MALE','male'),
        ('FEMALE','female'),
        ('OTHERS','others'),
        )
    gender=models.CharField(choices=gender_choices,max_length=10,null=True,blank=True)
    department_choices=(
        ('BCA','bca'),
        ('CS','cs'),
        ('EL','el'),
        ('BCOM','bcom'),
    )
    department=models.CharField(choices=department_choices,max_length=25,null=True,blank=True)
    phno=models.IntegerField(null=True,blank=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=10)
    profilepic=models.ImageField(upload_to='profilepic/',blank=True,null=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    name=models.CharField(max_length=200)
    date=models.DateField()
    description=models.TextField()
    def __str__(self):
        return self.name

class StudentGPA(models.Model):
        name=models.CharField(max_length=200)
        cgpa=models.FloatField()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

class internalmarklist(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      Name=models.CharField(max_length=200,null=True)
      Register_Number=models.CharField(max_length=200)
      Department=models.CharField(max_length=200)
      Android_Programming=models.CharField(max_length=200)
      Operating_System=models.CharField(max_length=200)
      Software_Testing=models.CharField(max_length=200)
      Computer_Networks=models.CharField(max_length=200)
      Project=models.CharField(max_length=200)

class internalexammarklist(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      Name=models.CharField(max_length=200,null=True)
      Register_Number=models.CharField(max_length=200)
      Department=models.CharField(max_length=200)
      Android_Programming=models.CharField(max_length=200)
      Operating_System=models.CharField(max_length=200)
      Software_Testing=models.CharField(max_length=200)
      Computer_Networks=models.CharField(max_length=200)
      Project=models.CharField(max_length=200)