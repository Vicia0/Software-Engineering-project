# Generated by Django 4.0.6 on 2022-12-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='the_ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.CharField(max_length=255)),
                ('car_plate', models.CharField(max_length=255)),
                ('car_color', models.CharField(max_length=255)),
                ('origin_area', models.CharField(max_length=255)),
                ('origin_stop', models.CharField(max_length=255)),
                ('destination_area', models.CharField(max_length=255)),
                ('destination_stop', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('available_seats', models.CharField(max_length=255)),
            ],
        ),
    ]
