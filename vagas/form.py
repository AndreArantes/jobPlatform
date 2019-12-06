from django.forms import ModelForm
from vagas.models import Vaga


class VagaForm(ModelForm):
    class Meta:
        model = Vaga
        fields = ['nome', 'escolaridade_minima', 'faixa_salarial', 'requisitos']
