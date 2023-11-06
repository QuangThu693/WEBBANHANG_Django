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

  def success_view(request):
    user = request.user  # Truy cập thông tin người dùng đã đăng nhập
    return render(request, 'registration/success.html', {'user': user})