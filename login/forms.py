from django import forms

 
class LoginForm(forms.Form):
	username = forms.CharField(label = "Enter Your Username")
 	pw = forms.CharField (widget =forms.PasswordInput, label ="Enter Your Password")