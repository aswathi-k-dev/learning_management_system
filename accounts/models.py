from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=15,unique=True)

    ROLE_CHOICES = (
        ("student","student"),
        ("trainer","trainer")
    )

    role = models.CharField(max_length=200,choices=ROLE_CHOICES,default="student")

class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passout_year = models.CharField(max_length=20,null=True)

    github_url = models.URLField(null=True)

    linkedin_url = models.URLField(null=True)

    profile_image = models.ImageField(upload_to="student",null=True)

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")


class TrainerProfile(models.Model):

    qualification = models.CharField(max_length=200,null=True)

    experience = models.IntegerField(null=True)

    skills = models.CharField(max_length=200, null=True)

    profile_image = models.ImageField(upload_to="trainer",null=True)

    trainer = models.OneToOneField(User,on_delete=models.CASCADE,related_name="trainer")

