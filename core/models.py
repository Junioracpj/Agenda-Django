from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)  # define o tamanho do campo,parametro titulo
    descricao = models.TextField(blank=True, null=True)  # parametro texto
    data_evento = models.DateTimeField(verbose_name='Data do Evento')  # parametro de data manual e automatico
    dat_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # importando usuario

    class Meta:
        db_table = 'evento'  # funcao dara o nome a tabela

    def __str__(self):
        return self.titulo  # Define o nome do evento como titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        return self.data_evento < datetime.now()

    def get_evento_que_falta_menos_de_1h(self):
        return self.data_evento - timedelta(hours=1) < datetime.now() < self.data_evento

