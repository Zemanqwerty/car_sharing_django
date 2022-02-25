from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ClientPhoto(models.Model):
    id_client_photo = models.AutoField(auto_created=True, primary_key=True)
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='user_img/', default='static/img/user/default.jpg')

    def __str__(self):
        return f'{self.id_client}'


class Car(models.Model):
    id_car = models.AutoField(auto_created=True, primary_key=True)
    car_image = models.ImageField(upload_to='car_img/')
    date_of_publication = models.DateField(auto_now_add=True)
    day_price = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    auto_brand = models.CharField(max_length=20)
    auto_model = models.CharField(max_length=40)
    color = models.CharField(max_length=30)
    condition = models.TextField()
    year = models.IntegerField()
    mileage = models.IntegerField()
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'г. {self.city}, {self.auto_brand} - {self.auto_model}'


class ClientCar(models.Model):
    id_client_car = models.AutoField(auto_created=True, primary_key=True)
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id_client} - {self.id_car}'


class Considerations(models.Model):
    id_consideration = models.AutoField(auto_created=True, primary_key=True)
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client_phone_number = models.IntegerField()
    status = models.CharField(default='На рассмотрении', max_length=56)
    date_of_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id_client} - {self.id_car}'
