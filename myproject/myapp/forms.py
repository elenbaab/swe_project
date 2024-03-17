from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class NewUserForm(forms.Form):
    start_year = forms.IntegerField(label='Start Year')
    grad_year = forms.IntegerField(label='Graduation Year')
    major1 = forms.CharField(label='Major 1', max_length=100, required=True)
    major2 = forms.CharField(label='Major 2', max_length=100, required=False)
    minor1 = forms.CharField(label='Minor 1', max_length=100, required=False)
    minor2 = forms.CharField(label='Minor 2', max_length=100, required=False)
    