from django import forms

class HelloForm(forms.Form):
  name = forms.CharField(label='樹種名')