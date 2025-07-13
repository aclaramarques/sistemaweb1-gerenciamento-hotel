from django.shortcuts import render, get_object_or_404, redirect
from .models import Quarto
from .forms import QuartoForm

def listar_quartos(request):
    quartos = Quarto.objects.all()
    return render(request, 'quartos/listar.html', {'quartos': quartos})

def cadastrar_quarto(request):
    form = QuartoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_quartos')
    return render(request, 'quartos/form.html', {'form': form})

def editar_quarto(request, id):
    quarto = get_object_or_404(Quarto, id=id)
    form = QuartoForm(request.POST or None, instance=quarto)
    if form.is_valid():
        form.save()
        return redirect('listar_quartos')
    return render(request, 'quartos/form.html', {'form': form})

def deletar_quarto(request, id):
    quarto = get_object_or_404(Quarto, id=id)
    quarto.delete()
    return redirect('listar_quartos')