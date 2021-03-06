from django import forms
from .models import Link
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class LinksForm(forms.ModelForm):
    original = forms.URLField(required=True)
    class Meta:
        model = Link
        fields = ["original"]

class UserForm(UserCreationForm):
    username = forms.CharField(min_length=8, max_length=150, help_text="")
    email = forms.EmailField(max_length=254, help_text="", required=True)
    password1 = forms.CharField(label="Password", help_text="", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", help_text="", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", )

class UserUpdateForm(UserChangeForm):
    username = forms.CharField(min_length=8, max_length=150, help_text="", required=False)
    email = forms.EmailField(max_length=254, help_text="", required=False)
    password = None

    class Meta:
        model = User
        fields = ["username", "email"]

class EditSlugForm(forms.Form):
    slug = forms.CharField(min_length=1)