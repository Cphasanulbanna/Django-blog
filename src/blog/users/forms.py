from dataclasses import fields
from django import forms
from django.contrib.auth.models import User


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]
        widgets = {
            "password" : forms.widgets.PasswordInput(attrs={"class":"hello hi", "placeholder":"Enter Password"})
        }
