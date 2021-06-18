from django.contrib import admin
from django.apps import apps
from pages.models import Agendamento
from django.db import models

# Register your models here.


class agendamentoAdmin(admin.ModelAdmin):
    list_display = ('agendamentoData','agendamentoHora','agendamentoNome')

admin.site.register(Agendamento)