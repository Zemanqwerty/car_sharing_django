# Generated by Django 3.2.7 on 2021-10-31 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_clientphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientphoto',
            name='photo',
            field=models.ImageField(default='static/img/user/default.jpg', upload_to='user_img/'),
        ),
    ]
