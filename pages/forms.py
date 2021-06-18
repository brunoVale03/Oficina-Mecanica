from django import forms  
from pages.models import Agendamento  #models.py
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Nome')
    last_name = forms.CharField(max_length=30, label='Sobrenome')
    cpf = forms.CharField(max_length=30, label='CPF')
    phone = forms.CharField(max_length=30, label='Telefone')
    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.cpf = self.cleaned_data['CPF']
        user.phone = self.cleaned_data['Telefone']
        user.save()
        return user
    
class Agendamento(forms.ModelForm):  
    class Meta:  
        model = Agendamento  
        fields = ['agendamentoData','agendamentoHora','agendamentoDescricao','agendamentoNome','agendamentoMarcado']