from django import forms


class UserLoginForm(forms.form):
    username = forms.CharField()
    password = forms.CharField()