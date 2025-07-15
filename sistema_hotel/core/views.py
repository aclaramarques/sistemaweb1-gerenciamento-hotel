from django.shortcuts import render, get_object_or_404, redirect
from quartos.models import Quarto
from clientes.models import Hospede
from reservas.models import Reserva


def listar_tudo(request):
    quartos = Quarto.objects.all()
    hospedes = Hospede.objects.all()
    reservas = Reserva.objects.all()
    return render(request, 'index.html', {'quartos': quartos, 'hospedes': hospedes, 'reservas' : reservas})