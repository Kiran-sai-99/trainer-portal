from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Enter your username here...'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Enter your password here...'
            }
        )
    )

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        label= 'Enter Password',
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Enter your password here...'
            }
        )
    )

    confirm_password = forms.CharField(
        label= 'ReEnter Password',
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Re-Enter your password here...'
            }
        )
    )

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password' ]
        
        widgets = {
            'username' : forms.TextInput(
                attrs={
                    'placeholder' : 'Enter your username here...'
                }
            ),

            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'Enter your email here...'
                }
            )
        }

    def clean_email(self):
        email = self.cleaned_data['email']

        if email and not email.endswith('@dcl.in'):
            raise forms.ValidationError('Email should end with @dcl.in')
    
        return email


    def clean_username(self):
        username = self.cleaned_data['username']
        #logic for checing whether username exists or not
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data['password']
        pwd2 = cleaned_data['confirm_password']

        if pwd != pwd2:
            raise forms.ValidationError('Passwords does not match!!!')

        return cleaned_data