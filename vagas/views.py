from django.shortcuts import render, redirect
from vagas.models import Vaga
from vagas.form import VagaForm
import datetime


def home(request):
    data = {}
    data['vagas'] = Vaga.objects.all()
    return render(request, 'vagas/home.html', data)


def nova_vaga(request):
    form = VagaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'vagas/cadastro_vaga.html', {'form': form})


def busca(request, pk):
    vaga = Vaga.objects.get(pk=pk)
    form = VagaForm(request.POST or None, instance=vaga)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'vagas/cadastro_vaga.html', {'form': form})
