from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user data-input',
            'placeholder': 'Username',
            'id': 'id-username'
        }
    ), required=True)
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-user data-input',
                'placeholder': 'Password',
                'id': 'login-password',
                'style': 'width: unset;'
            }
        ),
        required=True)
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput({
        'id': 'id_remember_me',
        'class': 'check-remember',
    }))

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that "
            "password may be case-sensitive."
        ),
    }
