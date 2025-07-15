
from django.shortcuts import render, redirect
from .forms import ReservaForm
from django.shortcuts import get_object_or_404, redirect
from .models import Reserva



def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/listar.html', {'reservas': reservas})

def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    form = ReservaForm(request.POST or None, instance=reserva)
    if form.is_valid():
        form.save()
        return redirect('listar_reservas')
    return render(request, 'reservas/form.html', {'form': form})

def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('listar_reservas')

def cadastrar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_reservas') 
    else:
        form = ReservaForm()

    return render(request, 'reservas/form.html', {'form': form})
