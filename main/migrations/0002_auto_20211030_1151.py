# Generated by Django 3.2.7 on 2021-10-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carphoto',
            name='photo',
            field=models.ImageField(upload_to='car_img/'),
        ),
        migrations.AlterField(
            model_name='clientphoto',
            name='photo',
            field=models.ImageField(upload_to='user_img/'),
        ),
    ]