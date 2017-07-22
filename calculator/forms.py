from django import forms

class get_sol(forms.Form):
	ans = forms.CharField(label='ans', max_length=100)