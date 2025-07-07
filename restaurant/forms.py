from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(required=True, widget=forms.PasswordInput())