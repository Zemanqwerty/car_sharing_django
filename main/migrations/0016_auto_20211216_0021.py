# Generated by Django 3.2.7 on 2021-12-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20211129_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcar',
            name='date_of_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='considerations',
            name='date_of_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
