from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.


# функция деавторизации пользователя
def logout_page(request):
    # проверка авторизации пользователя
    if request.user.is_authenticated:
        logout(request)
        return redirect('login_page')
    else:
        return redirect('login_page')


# функция авторизация пользователя
def login_page(request):
    from .forms import ClientLoginForm

    # проверка авторизации пользователя
    if request.user.is_authenticated:
        return redirect('index_page')
    else:
        if request.method == 'POST':
            form = ClientLoginForm(request.POST)
            if form.is_valid():
                user_email = request.POST['email']
                user_password = request.POST['password']

                user = authenticate(request, username=user_email, password=user_password)
                if user is not None:
                    login(request, user)
                    return redirect('index_page')
                else:
                    context = {
                        'form': form,
                        'response_to_user': 'Неправильный логин или пароль.',
                    }
                    return render(request, 'main/login_page.html', context)
            else:
                context = {
                    'form': form,
                    'response_to_user': 'Проверьте введённые данные.',
                }
                return render(request, 'main/login_page.html', context)
        else:
            form = ClientLoginForm
            return render(request, 'main/login_page.html', context={
                'form': form,
                'response_to_user': '',
            })


# функция регистрации пользователя
def register_page(request):
    from .forms import ClientRegisterForm
    from .models import User

    # проверка авторизации пользователя
    if request.user.is_authenticated:
        return redirect('index_page')
    else:
        if request.method == 'POST':
            form = ClientRegisterForm(request.POST)
            if form.is_valid():
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                password = request.POST['password']
                email = request.POST['email']
                check_user = User.objects.all().filter(email=email)
                if check_user:
                    context = {
                        'form': form,
                        'response_to_user': f'Пользователь {email} уже зарегистрирован.',
                    }
                    return render(request, 'main/register_page.html', context)
                else:
                    new_user = User.objects.create_user(username=email,
                                                        first_name=first_name,
                                                        last_name=last_name,
                                                        password=password,
                                                        email=email,)

                    new_user.save()
                    return redirect('login_page')
            else:
                context = {
                    'form': form,
                    'response_to_user': 'Проверьте введённые данные.',
                }
                return render(request, 'main/register_page.html', context)
        else:
            form = ClientRegisterForm

            context = {
                'form': form,
                'response_to_user': '',
            }
            return render(request, 'main/register_page.html', context)


# страница поддверждания почты пользователя
def check_user_mail(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass
        else:
            return render(request, 'main/check_mail.html', context={})
    else:
        return redirect('login_page')


# главная страница с активными объявлениями
def index_page(request):
    from django.db.models import Q
    from .models import ClientPhoto
    from .models import Car

    # проверка авторизации пользователя
    if request.user.is_authenticated:
        search = request.GET.get('query')
        if search:
            cars = Car.objects.all().filter(Q(auto_model__contains=search) |
                                                Q(auto_brand__contains=search))
            all_cars = cars.exclude(id_client=request.user)
            try:
                user_photo = ClientPhoto.objects.filter(id_client__username=request.user.username).values('photo')[0]
                context = {
                    'user_img': user_photo,
                    'cars': all_cars,
                }
                print(all_cars)
            except Exception as error:
                context = {'cars': all_cars, }
            return render(request, 'main/index_page.html', context)
        else:
            all_cars = Car.objects.all().exclude(id_client=request.user)
            try:
                user_photo = ClientPhoto.objects.filter(id_client__username=request.user.username).values('photo')[0]
                context = {
                    'user_img': user_photo,
                    'cars': all_cars,
                }
            except Exception as error:
                context = {'cars': all_cars, }
            return render(request, 'main/index_page.html', context)
    else:
        return redirect('login_page')


# страница аккаунта пользователя
def account_page(request):
    from .models import ClientPhoto
    from .models import Car
    from .forms import ClientPhotoForm

    # проверка авторизации пользователя
    if request.user.is_authenticated:
        user_cars = Car.objects.all().filter(id_client__username=request.user.username)

        try:
            user_photo = ClientPhoto.objects.filter(id_client__username=request.user.username).values('photo')[0]
            context = {
                'user_img': user_photo,
                'user_cars': user_cars,
            }
        except Exception as error:
            form = ClientPhotoForm

            context={
                'user_cars': user_cars,
                'form': form,
            }
        return render(request, 'main/account.html', context)
    else:
        return redirect('login_page')


def active_apply(request):
    from .models import Considerations, ClientPhoto
    from .forms import ClientPhotoForm

    if request.user.is_authenticated:
        f_r = Considerations.objects.all().filter(id_car__id_client=request.user, status='На рассмотрении')
        try:
            user_photo = ClientPhoto.objects.filter(id_client__username=request.user.username).values('photo')[0]
            context = {
                'user_img': user_photo,
                'list': f_r,
            }
        except Exception as error:
            form = ClientPhotoForm

            context = {
                'list': f_r,
                'form': form,
            }

        return render(request, 'main/active_apply.html', context)
    else:
        return redirect('login_page')


# функция зоздания аватарки пользователя
def user_img_upload(request):
    from .forms import ClientPhotoForm

    # проверка авторизации пользователя
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ClientPhotoForm(request.POST, request.FILES)
            if form.is_valid():
                user_img = form.save(commit=False)
                user_img.photo = request.FILES['photo']
                user_img.id_client = request.user
                user_img.save()
                return redirect('account_page')
        else:
            return redirect('index_page')
    else:
        return redirect('login_page')


# функция создания нового объявления
def create_car(request):
    from .forms import CarForm

    # проверка авторизации пользователя
    if request.user.is_authenticated:
        form = CarForm(request.POST, request.FILES)
        if request.method == 'POST':
            if form.is_valid():
                new_car = form.save(commit=False)
                new_car.car_image = request.FILES['car_image']
                new_car.id_client = request.user
                new_car.save()

                return redirect('account_page')
        else:
            return render(request, 'main/create_car.html', context={'form': CarForm})
    else:
        return redirect('login_page')


# функция удаления активного объявления
def delete_car(request, id_car):
    from .models import Car

    # проверка авторизации пользователя
    if request.user.is_authenticated:
        Car.objects.all().filter(id_car=id_car).delete()

        return redirect('account_page')
    else:
        return redirect('login_page')


# страница просмотра ифнормации об определённом автомобили
def car_view(request, id_car):
    from .models import Car
    from .forms import ConsiderationsForm

    # проверка авторизации пользователя
    if request.user.is_authenticated:
        cur_car = Car.objects.all().filter(id_car=id_car)[0]

        context = {
            'car': cur_car,
            'form': ConsiderationsForm,
        }

        return render(request, 'main/current_car_page.html', context)
    else:
        return redirect('login_page')


def consideration(request, id_car):
    from .forms import ConsiderationsForm
    from .models import Car, Considerations

    if request.user.is_authenticated:
        if request.method == 'POST':
            context = {}
            form = ConsiderationsForm(request.POST)
            if form.is_valid():
                car = Car.objects.all().filter(id_car=id_car)[0]

                #new_consideration = form.save(commit=False)
                #new_consideration.id_client = request.user
                #new_consideration.id_car = car
                #new_consideration.save()

                new_consideration = Considerations.objects.create(id_client=request.user,
                                                                  client_phone_number=request.POST.get('client_phone_number'),
                                                                  id_car=car)
                new_consideration.save()

                context = {
                    'response_ok': ('Ваша заявка будет рассмотренна '
                                    'владельцем объявления в '
                                    'ближайшее время'),
                }
            else:
                context = {
                    'response_error': 'Проверьте введённые данные',
                }

            return render(request, 'main/consideration_info.html', context=context)
        else:
            return redirect('index_page')
    else:
        return redirect('login_page')


def apply_accept(request, id_cons):
    from .models import Considerations, ClientCar
    from django.core.mail import send_mail
    from django.conf import settings
    from django.template.loader import get_template

    if request.user.is_authenticated:
        cons = Considerations.objects.get(id_consideration=id_cons)
        new_clientcar = ClientCar.objects.create(id_car=cons.id_car,
                                                 id_client=cons.id_client)
        new_clientcar.save()

        cons = Considerations.objects.get(id_consideration=id_cons)
        cons.status = 'Одобрен'
        cons.save()

        mail_notification = send_mail(
                'Поздравляем с успешной арендой!',
                '',
                settings.EMAIL_HOST_USER,
                [cons.id_client, cons.id_car.id_client],
                fail_silently=True,
                html_message=get_template(f'email/notification.html').render(context={
                    'car_brand': cons.id_car.auto_brand,
                    'car_model': cons.id_car.auto_model,
                    'client_information': cons.id_client,
                    'client_phone': cons.client_phone_number,
                    'owner_information': cons.id_car.id_client,
                })
            )

        return redirect('active_apply')
    else:
        return redirect('login_page')


def apply_delete(request, id_cons):
    from .models import Considerations

    if request.user.is_authenticated:
        cons = Considerations.objects.get(id_consideration=id_cons)
        cons.status = 'Не одобрен'
        cons.save()

        return redirect('active_apply')
    else:
        return redirect('login_page')


def apply_history(request):
    from .models import Considerations, ClientPhoto
    from .forms import ClientPhotoForm

    if request.user.is_authenticated:
        f_r = Considerations.objects.all().filter(id_car__id_client=request.user)
        try:
            user_photo = ClientPhoto.objects.filter(id_client__username=request.user.username).values('photo')[0]
            context = {
                'user_img': user_photo,
                'list': f_r,
            }
        except Exception as error:
            form = ClientPhotoForm

            context = {
                'list': f_r,
                'form': form,
            }

        return render(request, 'main/apply_history.html', context)
    else:
        return redirect('login_page')


def my_apply(request):
    from .models import Considerations, ClientPhoto
    from .forms import ClientPhotoForm

    if request.user.is_authenticated:
        f_r = Considerations.objects.all().filter(id_client=request.user)
        try:
            user_photo = ClientPhoto.objects.filter(id_client__username=request.user.username).values('photo')[0]
            context = {
                'user_img': user_photo,
                'list': f_r,
            }
        except Exception as error:
            form = ClientPhotoForm

            context = {
                'list': f_r,
                'form': form,
            }

        return render(request, 'main/my_apply.html', context)
    else:
        return redirect('login_page')
