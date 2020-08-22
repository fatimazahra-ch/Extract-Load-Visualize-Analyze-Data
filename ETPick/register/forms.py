from django import forms

class RegisterForm(forms.Form):
	firstName = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'First Name'}))
	lastName = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Last Name'}))
	city = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'City'}))
	country = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Country'}))
	email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Email'}))
	aboutYou = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control form-control-alternative', 'required': False, 'placeholder': 'A few words about you'}))
	company = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Company'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'required': False, 'placeholder': 'Password'}))
	confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'required': False, 'placeholder': 'Confirm Password'}))