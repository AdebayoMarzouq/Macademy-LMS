from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True, blank=True)


class Profile(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_no = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
