from django import forms
from .models import *

class CreateAuthorForm(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    patronymic = forms.CharField(max_length=20)
    birth_date = forms.DateField()
    bio = forms.CharField()
