from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('login/', views.login_page, name='login_page'),
    path('registration/', views.register_page, name='registration_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('account/', views.account_page, name='account_page'),
    path('user_img_upload/', views.user_img_upload, name='user_img_upload'),
    path('check_user_mail/', views.check_user_mail, name='check_,mail'),
    path('create_car/', views.create_car, name='create_car'),
    path('<int:id_car>/view/', views.car_view, name='car_view'),
    path('account/<int:id_car>/delete/', views.delete_car, name='delete_car'),
    path('<int:id_car>/view/consideration', views.consideration, name='consideration'),
    path('active_apply/', views.active_apply, name='active_apply'),
    path('active_apply/<int:id_cons>/accept/', views.apply_accept, name='apply_accept'),
    path('active_apply/<int:id_cons>/delete/', views.apply_delete, name='apply_accept'),
    path('my_apply/', views.my_apply, name='my_apply'),
    path('apply_history/', views.apply_history, name='apply_history'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

