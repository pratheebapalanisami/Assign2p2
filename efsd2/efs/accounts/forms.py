from accounts.models import CustomUser
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

class CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    address = forms.CharField(label='Address')
    city = forms.CharField(label='City')
    state = forms.CharField(label='State')
    zipcode = forms.CharField(label='Zipcode')
    phone_number = forms.CharField(label='Phone Number')
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'address', 'city', 'state', 'zipcode', 'phone_number')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


