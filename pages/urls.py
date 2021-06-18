from django.contrib import admin
from django.urls import path,include
from .views import home,comofunc,contato,cadastro,login,homecliente,agendamento
from pages import views

urlpatterns =[
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('home/',home,name='home'),
    path('contato/',contato,name='contato'),
    path('comofunc/',comofunc,name='comofunc'),
    path('cadastro/',cadastro,name='cadastro'),
    #path('password_change/',recuperacao,name='recuperacao'),
    path('homecliente/',homecliente,name='homecliente'),
    path('agendamento/',views.agendamento,name='agendamento'),
]