from django import forms

class InserirForm(forms.Form):
    quantidade = forms.IntegerField()