from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, EmailField, PasswordInput


class CustomUserCreationForm(Form):
    username = CharField(label='Enter Username', min_length=4, max_length=20)
    email = EmailField(label='Enter email')
    password = CharField(label='Enter password', widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        resp = User.objects.filter(username=username)
        if resp.count():
            raise ValidationError('Username is already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        resp = User.objects.filter(email=email)
        if resp.count():
            raise ValidationError('Email is already registered.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password'],
        )
        return user


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
