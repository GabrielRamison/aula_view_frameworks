from django.db import models
from .pessoa import Pessoa

class Passaporte(models.Model):
    numero = models.CharField(max_length=100, verbose_name='numero')
    data_criacao = models.DateField(verbose_name='data criacao')
    validade = models.DateField(verbose_name='validade')
    dono = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "{}:{} - {} - {}".format(self.numero, self.data_criacao, self.validade, self.dono)