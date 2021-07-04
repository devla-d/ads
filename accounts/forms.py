from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth  import login,authenticate,logout
 

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    is_advertiser = forms.BooleanField(
        label = "Want to advertise",
        required = False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'
                                     })
    )
      
    class Meta:
        model = Account
        fields = ['username','email','phone','password1','password2','is_advertiser']





class LoginForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ['username','password']

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password =  self.cleaned_data['password']
            if not authenticate(username=username,password=password):
                raise forms.ValidationError('Invalid Credentials')


