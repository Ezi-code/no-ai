from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(label="email", max_length=50)
	password = forms.CharField(label="password")

class RegisterForm(forms.Form):
	email = forms.EmailField(label="email", max_length=50)
	username = forms.CharField(label="username", max_length=150)
	password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password"}))
	confirm_password = forms.CharField(label="confirm password", max_length=150)
