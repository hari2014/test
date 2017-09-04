from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserChangeForm
from hello.models import detail,login


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )


class info(forms.ModelForm):
    username=forms.CharField(required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.CharField(required=True)
    password=forms.CharField(required=True)
    phone=forms.CharField(required=True)

    class Meta:
        model = detail
        fields = ('first_name', 'last_name', 'email', 'password','phone')


class check(forms.ModelForm):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True)
    class Meta:
        model=login
        fields=('username','password')