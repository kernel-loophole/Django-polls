from django import forms
from django.forms import fields
from .models import user,uploadfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class createuser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class user_form(forms.ModelForm):
    class Meta:
        model=user
        fields=[
            'email',
            'passwd',
            'name',
        ]
        widgets = {
        'password': forms.PasswordInput(attrs={'class': 'form-control', 'name': 'username'}),
        'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'name', 'placeholder': 'username'}),
       'email': forms.TextInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'email'}),
        }
class name_user(forms.Form):
    name=forms.CharField(label='name',max_length=100)
    roll_no=forms.IntegerField(label='roll_no',max_value=100)
class UploadFileForm(forms.ModelForm):
    class Meta:
        model=uploadfile
        fields=[
            'file_name',
        ]