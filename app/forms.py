from django import forms

class formulario(forms.Form):
    nome = forms.CharField(max_length=50)
    idade = forms.IntegerField  