from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Employee


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adını veya şifreyi yanlış girdiniz!")
        return super(LoginForm, self).clean()


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
            'e_phone',
            'e_date_left',
            'e_qualification',
        ]








class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Username')
    password1 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor!")
        return password2