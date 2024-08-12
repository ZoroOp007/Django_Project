from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from django import forms
from .models import Record



# - Register a User 

class CreateUserForm(UserCreationForm):
   
    class Meta:
        model = User
        fields= ['username','password1','password2']

    

# Login a User

class LoginForm(AuthenticationForm):
   
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


# -- Create Record Form

class AddRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name','last_name', 'email', 'phone', 'address', 'city', 'province','country']


# -- Update Record Form

class AddUpdateForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name','last_name', 'email', 'phone', 'address', 'city', 'province','country']