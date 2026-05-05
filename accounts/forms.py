from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

    def clean_password2(self):
        password = self.cleaned_data.get("password2")
        return password