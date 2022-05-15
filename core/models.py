from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)  # define o tamanho do campo,parametro titulo
    descricao = models.TextField(blank=True, null=True)  # parametro texto
    data_evento = models.DateTimeField(verbose_name='Data do Evento')  # parametro de data manual e automatico
    dat_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  #importando usuario

    class Meta:
        db_table = 'evento'  # funcao dara o nome a tabela

    def __str__(self):
        return self.titulo  # Define o nome do evento como titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')


