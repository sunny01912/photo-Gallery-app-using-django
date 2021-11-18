
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth.forms import AuthenticationForm,UsernameField,PasswordChangeForm,UserCreationForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
    )

class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        field_classes = {'username': UsernameField}
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})

        }