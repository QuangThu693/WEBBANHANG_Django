from django.shortcuts import render
from django import forms
from django.views import View
from .models import CustomerUser

# Create your views here.
class Registration(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Mật khẩu phải có ít nhất 8 ký tự.")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email này đã được sử dụng.")
        return email


