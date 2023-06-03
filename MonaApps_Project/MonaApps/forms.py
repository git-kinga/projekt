from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Token

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
        widget=forms.EmailInput(attrs={
            'type': 'username',
            'placeholder': 'username'
        }))
    password = forms.CharField(max_length=100,
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'placeholder': 'Password'
        }))

class RegistrationForm(UserCreationForm):
    username=forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Name'
        }))
    email = forms.CharField(max_length=100,
        widget=forms.EmailInput(attrs={
            'type': 'email',
            'placeholder': 'Email'
        }))
    password1 = forms.CharField(max_length=100,
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'placeholder': 'Password',
            'id': 'passwordChecker',
            'required class': 'password-input'
        }))
    password2 = forms.CharField(max_length=100,        
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'placeholder': 'Confirm Password'
        }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        if commit:
            user.save()
            
            #Create Token object
            Token.objects.create(user=user)
        
        return user