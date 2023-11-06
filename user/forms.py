from django import forms
from .models import CustomerUser

class RegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = CustomerUser
    fields = ['username', 'email', 'password', 'phone_number', 'address']

  def clean_phone_number(self):
    phone_number = self.cleaned_data['phone_number']
    if not phone_number.isnumeric() or len(phone_number) < 10:
      raise forms.ValidationError("Số điện thoại không hợp lệ")
    return phone_number

class LoginForm(forms.Form):
  username = forms.CharField(label="Tên đăng nhập")
  password = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput)