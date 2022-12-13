# Generated by Django 4.0.6 on 2022-12-13 08:15

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='approved_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_id', models.CharField(max_length=255)),
                ('driver', models.CharField(max_length=255)),
                ('passenger', models.CharField(max_length=255)),
                ('current_area', models.CharField(max_length=255)),
                ('current_stop', models.CharField(max_length=255)),
                ('destination_area', models.CharField(max_length=255)),
                ('destination_stop', models.CharField(max_length=255)),
                ('d_date', models.CharField(max_length=255)),
                ('d_time', models.CharField(max_length=255)),
                ('number_of_people', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='denied_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_id', models.CharField(max_length=255)),
                ('driver', models.CharField(max_length=255)),
                ('passenger', models.CharField(max_length=255)),
                ('current_area', models.CharField(max_length=255)),
                ('current_stop', models.CharField(max_length=255)),
                ('destination_area', models.CharField(max_length=255)),
                ('destination_stop', models.CharField(max_length=255)),
                ('d_date', models.CharField(max_length=255)),
                ('d_time', models.CharField(max_length=255)),
                ('number_of_people', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ride_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_id', models.CharField(max_length=255)),
                ('driver', models.CharField(max_length=255)),
                ('passenger', models.CharField(max_length=255)),
                ('current_area', models.CharField(max_length=255)),
                ('current_stop', models.CharField(max_length=255)),
                ('destination_area', models.CharField(max_length=255)),
                ('destination_stop', models.CharField(max_length=255)),
                ('d_date', models.CharField(max_length=255)),
                ('d_time', models.CharField(max_length=255)),
                ('number_of_people', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='the_ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.CharField(max_length=255)),
                ('origin_area', models.CharField(max_length=255)),
                ('origin_stop', models.CharField(max_length=255)),
                ('destination_area', models.CharField(max_length=255)),
                ('destination_stop', models.CharField(max_length=255)),
                ('car_plate', models.CharField(max_length=255)),
                ('car_color', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('available_seats', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='the_rideForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_plate', models.CharField(max_length=255)),
                ('car_color', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('available_seats', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='the_trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger', models.CharField(max_length=255)),
                ('current_area', models.CharField(max_length=255)),
                ('current_stop', models.CharField(max_length=255)),
                ('destination_area', models.CharField(max_length=255)),
                ('destination_stop', models.CharField(max_length=255)),
                ('d_date', models.CharField(max_length=255)),
                ('d_time', models.CharField(max_length=255)),
                ('number_of_people', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='the_tripForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_date', models.DateField()),
                ('d_time', models.TimeField()),
                ('number_of_people', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_passenger', models.BooleanField(default=False, verbose_name='Passenger')),
                ('is_driver', models.BooleanField(default=False, verbose_name='Driver')),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
