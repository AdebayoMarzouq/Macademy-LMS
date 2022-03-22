from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CustomUser(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True, blank=True)


class Profile(models.Model):
    DEFAULT_PK = 1
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/%Y/%m/%d', default='default.png')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_no = PhoneNumberField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = CountryField()

    def __str__(self):
        return f'{self.user}'
