from django import forms

from signupform.models import Signup

class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ['name', 'email', 'pw']

		def clean(self):
			cleaned_data = self.cleaned_data
			
			name = cleaned_data.get("name")
			email =cleaned_data.get("email")
			pw = cleaned_data.get("pw")
