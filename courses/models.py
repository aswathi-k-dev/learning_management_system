from django.db import models
from accounts.models import User

# Create your models here.

class Course(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    language = models.CharField(max_length=50)

    fee = models.DecimalField(max_digits=10, decimal_places=2)

    duration = models.CharField(max_length=50)

    category = models.CharField(max_length=100)

    cover_picture = models.ImageField(upload_to="cover_pics",null=True)

    trainer = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title