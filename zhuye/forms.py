from django import forms

class AddForm(forms.Form):
	domain = forms.CharField(max_length=100)
