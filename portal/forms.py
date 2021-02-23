from django import forms
from . import models
from django.contrib.auth.models import User

class ArticleFileForm(forms.ModelForm):
    class Meta:
        model = models.Article
        exclude = ['uploaded_by', 'last_edited']
        # widgets = { 'name':forms.TextInput(
        #     attrs={
        #         'class':"form-control",
        #         'id':"articlename",
        #         'placeholder':"Name of Paper"
        #     })
        # }
class ProfileCompleteForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['user_type', 'academic_status', 'description']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Id'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))