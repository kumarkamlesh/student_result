from django.db import models


# from passlib.hash import pbkdf2_sha256

# Create your models here.
# class admin_login(models.Model):
#     email=models.CharField(max_length=30)
#     password=models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.email


# registration form

class registration_form1(models.Model):
    username = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    dob = models.CharField(max_length=25)
    mobile = models.IntegerField()
    address = models.CharField(max_length=25)

    def __str__(self):
        return self.username
    # def verify_password(self,raw_password):
    #     return pbkdf2_sha256.verify(raw_password,self.password)


# add student
class add_stu(models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    course = models.CharField(max_length=10)
    branch = models.CharField(max_length=15)
    sem = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    dob = models.CharField(max_length=25)
    mobile = models.IntegerField()
    roll = models.IntegerField()

    def __str__(self):
        return self.username


class admin_view(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.email


class final_result(models.Model):
    roll_no = models.IntegerField()
    student_name = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    sub1 = models.CharField(max_length=50)
    sub2 = models.CharField(max_length=50)
    sub3 = models.CharField(max_length=50)
    sub4 = models.CharField(max_length=50)
    sub5 = models.CharField(max_length=50)
    sub6 = models.CharField(max_length=50)
    sub7 = models.CharField(max_length=50)
    sub8 = models.CharField(max_length=50)
    sub9 = models.CharField(max_length=50)
    marks = models.IntegerField()
    marks2 = models.IntegerField()
    marks3 = models.IntegerField()
    marks4 = models.IntegerField()
    marks5 = models.IntegerField()
    marks6 = models.IntegerField()
    marks7 = models.IntegerField()
    marks8 = models.IntegerField()
    marks9 = models.IntegerField()
    seminar = models.IntegerField()
    total = models.IntegerField()
    percentage = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.roll_no)


class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    contact_num = models.IntegerField()
    messaged = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
