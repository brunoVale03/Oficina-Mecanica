from django.db import models

class Agendamento(models.Model):
    agendamentoData = models.DateField()
    agendamentoHora = models.TimeField()
    agendamentoDescricao = models.TextField()
    agendamentoNome = models.TextField()
    
    TRUE_FALSE_CHOICES = (
    (1,'Confirmado'),
    (0,'Aguardando confirmação')
)
    
    agendamentoMarcado = models.CharField(max_length=1,choices = TRUE_FALSE_CHOICES)
    list_display = ('agendamentoData','agendamentoHora','agendamentoMarcado')
    class Meta:
        db_table = "agendamento"
        ordering = ['agendamentoData','agendamentoHora']
    def __str__(self):
        return f'{self.agendamentoData},{self.agendamentoHora},{self.agendamentoMarcado}'
    
agendamento = Agendamento.objects.all()