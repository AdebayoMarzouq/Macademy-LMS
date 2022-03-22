from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


def get_admin_user():
    # return get_user_model().objects.get_or_create(username='deleted')[0]
    return get_user_model().objects.get_or_create(pk=1)


class Course(models.Model):
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses_tutored',
                              on_delete=models.SET(get_admin_user))
    co_tutor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses_cotutored',
                                 on_delete=models.SET(get_admin_user))
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_joined', blank=True)
    Category = models.ManyToManyField(Category, related_name='courses')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DurationField(db_index=True)
    total_time = models.TimeField(blank=True, auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


# Create your models here.
