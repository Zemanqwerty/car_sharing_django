# Generated by Django 3.2.7 on 2021-10-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211030_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientphoto',
            name='photo',
            field=models.ImageField(default='static/img/user/default.jpg', upload_to='user_img/'),
        ),
    ]