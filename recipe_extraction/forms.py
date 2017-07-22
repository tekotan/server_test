from django import forms

class get(forms.Form):
	recipe = forms.CharField(label='recipe', max_length=10000)