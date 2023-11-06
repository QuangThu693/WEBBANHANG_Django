from django import forms
from .models import CustomerUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomerUser
        fields = ['username', 'email', 'password', 'phone_number', 'address']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        # Thực hiện kiểm tra và xác thực dữ liệu cho số điện thoại
        # Ví dụ: Kiểm tra xem số điện thoại có đúng định dạng không
        if not phone_number.isnumeric() or len(phone_number) < 10:
            raise forms.ValidationError("Số điện thoại không hợp lệ")
        return phone_number