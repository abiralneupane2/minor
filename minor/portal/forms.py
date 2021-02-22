from django import forms
from . import models

class ArticleFileForm(forms.ModelForm):
    class Meta:
        model = models.Article
        exclude = ['uploaded_by', 'last_edited']
        widgets = { 'name':forms.TextInput(
            attrs={
                'class':"form-control",
                'id':"articlename",
                'placeholder':"Name of Paper"
            })
        }
    
    # def clean_attachment(self):
    #     if self.cleaned_data['document'].name.split('.')[1] is not "pdf":
    #         raise forms.ValidationError('This file is not allowed.')
    #     return self.cleaned_data['document']