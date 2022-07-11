from django import forms
from django.forms import ModelForm
from .models import Links


class LinkForm(ModelForm):
    class Meta:
        model = Links
        fields = ['input_link', ]
        widgets = {
            'input_link': forms.TextInput(attrs={'placeholder': 'Введите ссылку для сокращения'}),
        }

        labels = {
            'input_link': '',
        }
