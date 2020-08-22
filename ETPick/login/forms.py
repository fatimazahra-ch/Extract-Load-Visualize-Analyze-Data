from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'required': False, 'placeholder': 'Password'}))
	