# Generated by Django 3.2.7 on 2021-11-29 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_car_day_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcar',
            name='date_of_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 22, 21, 49, 33030)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='considerations',
            name='date_of_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 22, 22, 7, 861770)),
            preserve_default=False,
        ),
    ]