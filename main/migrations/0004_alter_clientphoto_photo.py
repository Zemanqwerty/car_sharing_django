# Generated by Django 3.2.7 on 2021-10-31 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_clientphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientphoto',
            name='photo',
            field=models.ImageField(upload_to='user_img/'),
        ),
    ]