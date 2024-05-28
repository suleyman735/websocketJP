from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import UserAccount


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserAccount
        fields = ('username', 'password',)


class AddUserForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('email', 'name', 'role', 'password',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'password': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('email', 'name', 'role',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }