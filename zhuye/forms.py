from django import forms

class AddForm(forms.Form):
	domain = forms.CharField(label="报障域名", max_length=100,)
