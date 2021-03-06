# Generated by Django 4.0.3 on 2022-03-22 13:18

import course.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time', models.DurationField(db_index=True)),
                ('total_time', models.TimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ManyToManyField(related_name='courses', to='course.category')),
                ('co_tutor', models.ForeignKey(on_delete=models.SET(course.models.get_admin_user), related_name='courses_cotutored', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(on_delete=models.SET(course.models.get_admin_user), related_name='courses_tutored', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
