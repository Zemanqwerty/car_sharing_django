from django.shortcuts import render, redirect
from main.models import User, Car
# Create your views here.


def admin_index_page(request):
    if request.user.is_staff:
        search = request.GET.get('search')
        if search:
            active_users = User.objects.all().filter(username__contains=search)

            context = {'users_list': active_users}
        else:
            active_users = User.objects.all()

            context = {'users_list': active_users}
        return render(request, 'admin/login_page.html', context)
    else:
        return redirect('/')


def user_car_list(request, username):
    if request.user.is_staff:
        car_list = Car.objects.all().filter(id_client__username=username)

        context = {
            'username': username,
            'car_list': car_list,
        }

        return render(request, 'admin/user_car_list.html', context)
    else:
        return redirect('/')


def view_car_info(request, username, id_car):
    from main.models import Considerations, ClientCar, Car

    if request.user.is_staff:
        car = Car.objects.all().filter(id_car=id_car).first()
        considerations_list = Considerations.objects.all().filter(id_car=id_car)
        deal = ClientCar.objects.all().filter(id_car=id_car)

        context = {
            'cons_list': considerations_list,
            'deals_list': deal,
            'car': car,
            'username': username,
        }

        return render(request, 'admin/car_information.html', context)
    else:
        return redirect('/')
