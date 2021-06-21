from django.shortcuts import render
from pages.models import Agendamento 
from .models import Agendamento
#from django.contrib import messages

from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Agendamento WHERE agendamentoNome = %s", [self.baz])
        row = cursor.fetchone()
    return row

def home(request):
    return render(request,'homeindex.html')

def comofunc(request):
    return render(request,'comofunindex.html')

def contato(request):
    return render(request,'contatoindex.html')

def cadastro(request):
    return render(request,'cadastroindex.html')

def login(request):
    return render(request,'loginindex.html')

def homecliente(request):
    lista_agendamento = Agendamento.objects.all().filter(agendamentoNome=request.user.email)
    return render(request,'aclienteindex.html',{'lista_agendamento': lista_agendamento})

def agendamento(request):
    if request.method == 'POST':
        agendament = Agendamento(agendamentoData=request.POST,agendamentoHora=request.POST,agendamentoDescricao=request.POST,agendamentoNome=request.POST,agendamentoMarcado=0)
        if request.POST.get('agendamentoData') and request.POST.get('agendamentoHora') and request.POST.get('agendamentoDescricao') and request.POST.get('agendamentoNome'):
            agendament.agendamentoData= request.POST.get('agendamentoData')
            agendament.agendamentoHora= request.POST.get('agendamentoHora')
            agendament.agendamentoDescricao= request.POST.get('agendamentoDescricao')
            agendament.agendamentoNome=request.POST.get('agendamentoNome')
            agendament.save()
        else:
            return render(request,'agclienteindex.html')        
    return render(request,'agclienteindex.html')

