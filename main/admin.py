from django.contrib import admin
from .models import ClientPhoto, ClientCar, Car, Considerations

# Register your models here.


admin.site.register(ClientCar)
admin.site.register(ClientPhoto)
admin.site.register(Car)
admin.site.register(Considerations)
