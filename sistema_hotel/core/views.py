from django.shortcuts import render, get_object_or_404, redirect
from quartos.models import Quarto
from clientes.models import Hospede

def listar_tudo(request):
    quartos = Quarto.objects.all()
    hospedes = Hospede.objects.all()
    return render(request, 'index.html', {'quartos': quartos, 'hospedes': hospedes})