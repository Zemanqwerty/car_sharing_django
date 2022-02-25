from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, NumberInput, FileInput, Textarea
from .models import User, ClientPhoto, Car, Considerations


class ClientLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['password', 'email']

        widgets = {
            'password': PasswordInput(attrs={
                'class': 'login_user_form',
                'placeholder': 'Password',
            }),
            'email': EmailInput(attrs={
                'class': 'login_user_form',
                'placeholder': 'Email',
            })
        }


class ClientRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password',  'email']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'login_user_form',
                'placeholder': 'First name',
            }),
            'last_name': TextInput(attrs={
                'class': 'login_user_form',
                'placeholder': 'Last name',
            }),
            'password': PasswordInput(attrs={
                'class': 'login_user_form',
                'placeholder': 'Password',
            }),
            'email': EmailInput(attrs={
                'class': 'login_user_form',
                'placeholder': 'Email',
            }),
        }


class ClientPhotoForm(ModelForm):
    class Meta:
        model = ClientPhoto

        fields = ['photo']

        widgets = {
            'photo': FileInput(attrs={
                'class': 'user_img_input',
                'value': 'Загрузить фото',
            })
        }


class CarForm(ModelForm):
    class Meta:
        model = Car

        fields = ['car_image', 'address', 'city', 'district',
                  'auto_model', 'auto_brand', 'color',
                  'condition', 'year', 'mileage', 'day_price']

        widgets = {
            'car_image': FileInput(attrs={
                'class': 'car_image_input',
                'value': 'Обложка объявления'
            }),
            'city': TextInput(attrs={
                'class': 'car_text_input',
                'placeholder': 'Город, в котором располагается автомобиль'
            }),
            'district': TextInput(attrs={
                'class': 'car_text_input',
                'placeholder': 'Район города'
            }),
            'auto_model': TextInput(attrs={
                'class': 'car_text_input',
                'placeholder': 'Модель автомобиля'
            }),
            'auto_brand': TextInput(attrs={
                'class': 'car_text_input',
                'placeholder': 'Марка автомобиля'
            }),
            'color': TextInput(attrs={
                'class': 'car_text_input',
                'placeholder': 'Цвет автомобиля'
            }),
            'year': NumberInput(attrs={
                'class': 'car_text_input',
                'placeholder': 'Год выпуска автомобиля'
            }),
            'day_price': NumberInput(attrs={
                'class': 'car_text_input',
                'placeholder': 'Стоимость аренды за сутки'
            }),
            'condition': Textarea(attrs={
                'class': 'car_text_input',
                'placeholder': 'Опишите состояние автомобиля'
            }),
            'mileage': NumberInput(attrs={
                'class': 'car_text_input',
                'placeholder': 'Пробег'
            }),
            'address': TextInput(attrs={
                'class': 'car_text_input',
                'placeholder': 'Адрес, по которому располагается автомобиль'
            })
        }


class ConsiderationsForm(ModelForm):
    class Meta:
        model = Considerations

        fields = ['client_phone_number']

        widgets = {
            'client_phone_number': NumberInput(attrs={
                'class': 'input_phonenumber',
                'placeholder': '* контактный номер телефона',
            })
        }
