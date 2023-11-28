from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    full_name=forms.CharField(max_length=50)
    phone_number=forms.CharField(max_length=20)
    password1= forms.CharField(label='password',max_length=20,widget=forms.PasswordInput(attrs={'class':'form_control','placeholder':'Enter your password'}))
    password2= forms.CharField(label='confirm password',max_length=20,widget=forms.PasswordInput(attrs={'class':'form_control','placeholder':'Enter your password'}))

    def clean(self):
        cd=super().clean()
        p1=cd.get('password1')
        p2=cd.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError('password must match')

class UserLoginForm(forms.Form):
    full_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Enter your full_name'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form_control','placeholder':'Enter your password'}))






