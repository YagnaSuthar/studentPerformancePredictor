from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Teacher(models.Model):
    SUBJECT_CHOICES = [('p','physics'),('m','maths'),('c','chemistry')]

    host = models.ForeignKey(User,on_delete=models.CASCADE)
    teacher_id= models.AutoField(primary_key=True)
    subject = models.CharField(max_length=1,choices=SUBJECT_CHOICES,default='Unknown')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class student(models.Model):

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    teacher_id = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30,default='abc@gmail.com')
    date_of_birth = models.DateField(default='2000-01-01')
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='Unknown')
    name = models.CharField(max_length=100)
    pat_score = models.IntegerField(max_length=5)
    sat_score = models.IntegerField(max_length=5)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    




# srudent ->
#       student_id (Unique for all the students)
#       name (FirstName,LastName)
#       Email(Email Verification SMTP)
#       DOB
#       in views - student create and delete(CRUD) & read (performance) options are there


    