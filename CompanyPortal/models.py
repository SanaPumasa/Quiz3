from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class jobOpenings(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

class accounts(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.CharField()
    email = models.CharField()
    phone_number = models.IntegerField()
    joined_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    staff = models.BooleanField()
    admin = models.BooleanField()

    def __str__(self):
        return str(self.title)