from django import forms

from signup.models import Signup

class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ['name', 'email', 'password']

	def clean(self):
		cleaned_data = self.cleaned_data		
		name = cleaned_data.get("name")
		email =cleaned_data.get("email")
		password = cleaned_data.get("password")
