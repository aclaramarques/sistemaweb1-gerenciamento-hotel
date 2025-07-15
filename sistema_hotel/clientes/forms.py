from django import forms
from .models import Hospede

class HospedeForm(forms.ModelForm):
    class Meta:
        model = Hospede
        fields = ['nome', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'})
        }