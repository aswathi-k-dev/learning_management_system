from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.mail import send_mail
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

from django.db.models.signals import post_save

def create_student_profile(sender,instance,created,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(student = instance)

post_save.connect(create_student_profile,sender=User)


def create_trainer_profile(sender,instance,created,**kwargs):

    if created and instance.role == "trainer":

        TrainerProfile.objects.create(trainer = instance)

post_save.connect(create_trainer_profile,sender=User)



def send_invitaion_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        send_mail(
        'Account Creation Confirmation',
        'you have succesfully created a student account in LMS system.',
        'aswathik655@gmail.com',
        ['aswathisunil006@gmail.com'],
    )

    elif created and instance.role == "trainer":

        send_mail(
        'Account Creation Confirmation',
        'you have succesfully created a trainer account in LMS system.',
        'aswathik655@gmail.com',
        ['aswathisunil006@gmail.com'],
    )

post_save.connect(send_invitaion_mail,sender=User)




