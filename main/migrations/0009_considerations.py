# Generated by Django 3.2.7 on 2021-11-21 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_delete_carphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Considerations',
            fields=[
                ('id_consideration', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
