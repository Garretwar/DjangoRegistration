from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Форма для реєстрації
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

# Форма для авторизації
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
