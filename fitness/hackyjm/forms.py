from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserInfo


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('country_code', 'ph_num', 'pay_num')
