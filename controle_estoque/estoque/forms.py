from django import forms

class InserirForm(forms.Form):
    tipo = forms.CharField(max_length = 20)
    tamanho = forms.CharField(max_length = 2)
    core = forms.CharField(max_length = 20)
    quantidade = forms.IntegerField()