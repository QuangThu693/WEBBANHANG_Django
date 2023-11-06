from django import forms
from .models import CustomerUser

class Registration(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
      model = CustomerUser
      fields = ['username', 'email', 'password', 'phone_number',]