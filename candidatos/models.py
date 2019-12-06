from django.db import models
from django.utils.translation import gettext_lazy as _


class Candidato(models.Model):
    nome = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    senha = models.CharField(max_length=32)

    class Salario(models.IntegerChoices):
        FAIXA1 = 1, _('ate 1.000')
        FAIXA2 = 2, _('de 1.000 a 2.000')
        FAIXA3 = 3, _('de 2.000 a 3.000')
        FAIXA4 = 4, _('acima de 3.000')

    pretensao_salarial = models.IntegerField(choices=Salario.choices, default=Salario.FAIXA1)
    experiencia = models.TextField(null=True)

    class Escolaridade(models.TextChoices):
        ENSINOFUDAMENTAL = 'EF', _('Ensino Fundamental')
        ENSINOMEDIO = 'EM', _('Ensino Médio')
        TECNOLOGO = 'TC', _('Tecnólogo')
        ENSINOSUPERIOR = 'ES', _('Ensino Superior')
        POSMBAMESTRADO = 'PM', _('Pós / MBA / Mestrado')
        DOUTORADO = 'DR', _('Doutorado')

    nivel_escolaridade = models.CharField(
        max_length=2,
        choices=Escolaridade.choices,
        default=Escolaridade.ENSINOFUDAMENTAL,
    )
