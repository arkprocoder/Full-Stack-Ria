from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.
class Register(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    fatherName=models.CharField(max_length=20)
    phoneNumber=models.CharField(max_length=14)
    alternateNumber=models.CharField(max_length=14)
    email=models.EmailField(primary_key=True)
    collegeName=models.CharField(max_length=100)
    address=models.TextField(max_length=150)
    landmark=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField()
    companyName=models.CharField(max_length=150,blank=True,null=True)
    designation=models.CharField(max_length=150)
    qualification=models.CharField(max_length=100)
    computerKnowledge=models.CharField(max_length=50)
    Course=models.TextField(max_length=350,blank=True,null=True)
    timestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.email

class Courses(models.Model):
    courseName=models.CharField(max_length=150)
    image=models.ImageField(upload_to="course",blank=True,null=True)
    courseFee=models.IntegerField()
    courseDuration=models.IntegerField()
    syllabus=RichTextField(default="syllabus")
    aboutCourse=RichTextField(default="aboutCourse")

    def __str__(self):
        return self.courseName

class Payments(models.Model):
    name=models.ForeignKey(Register,on_delete=models.CASCADE)
    amountPaid=models.IntegerField()
    balance=models.IntegerField(blank=True,null=True)
    status= models.CharField(max_length=20,default="Unpaid")
    def __str__(self):
        return self.name

class Documents(models.Model):
    email=models.ForeignKey(Register,on_delete=models.CASCADE)
    document=models.ImageField(upload_to='documents')
    verification=models.BooleanField(default=False)
    def __str__(self):
        return self.email


class Certificate(models.Model):
    email=models.ForeignKey(Register,on_delete=models.CASCADE)
    certificate=models.ImageField(upload_to='certificates')
    def __str__(self):
        return self.email
