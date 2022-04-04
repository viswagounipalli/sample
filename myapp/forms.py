from myapp.models import register
from django import forms

class register_form(forms.ModelForm):
	class Meta:
		model=register
		#fields=["firstname","lastname","email","address","password"]
		fields="__all__"
		widgets={
		'password':forms.PasswordInput()
		}

class login_form(forms.Form):
	username=forms.CharField(max_length=100)
	password=forms.CharField(max_length=32,widget=forms.PasswordInput())

	"""class Meta:
		model=register
		fields=["firstname","password"]
		widgets={
		"password":forms.PasswordInput()
		}
	"""

