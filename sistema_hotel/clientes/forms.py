from django import forms
from .models import Hospede

class HospedeForm(forms.ModelForm):
    model = Hospede
    fields = ['nome', 'telefone', 'dataNasc']