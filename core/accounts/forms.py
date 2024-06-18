from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=250)  # Email field with max length 250
    
    class Meta:
        model = User  # Associate this form with the User model
        fields = ('email', 'password1', 'password2', )  # Fields to include in the form
