from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.admin_index_page, name='admin_index_page'),
    path('<str:username>/car_list', views.user_car_list, name='user_car_list'),
    path('<str:username>/<int:id_car>/view_info', views.view_car_info, name='car_info'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

