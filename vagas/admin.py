from django.contrib import admin
from vagas.models import Vaga
from candidatos.models import Candidato

admin.site.register(Vaga)
admin.site.register(Candidato)
