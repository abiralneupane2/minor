from django import forms
from . import models
from django.contrib.auth.models import User

def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class ProfileCompleteForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ('full_name', 'user_type', 'academic_status', 'description',)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

class PasswordChangeForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Retype Password'}))
    class Meta:
        model = User
        fields = ('password',)
    def clean(self):
        clean(self)

class RegistrationForm(forms.ModelForm):
    full_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Full Name'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Retype Password'}))
    class Meta:
        model=User
        fields=('username','email','password')
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Id'}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter Email'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'})
        }

    def clean(self):
        clean(self)
class ArticleForm(forms.ModelForm):
    collaborators = forms.ModelMultipleChoiceField(queryset=models.Person.objects.all(),widget=forms.CheckboxSelectMultiple, required=False)
    class Meta:
        model = models.Article
        fields = ['name', 'doc_type']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Id'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))

class ArticleFileForm(forms.ModelForm):
    class Meta:
        model = models.Files
        fields = ('file',)
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True})
        }

