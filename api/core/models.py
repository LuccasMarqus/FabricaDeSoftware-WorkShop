from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=140, null=True)
    endereco = models.CharField(max_length=200, null=True)
    pedido = models.CharField(max_length=200, null=True)
    dataPrevista = models.DateField(null=True)
    anotacoes = models.TextField(null=True)
    
    def __str__(self):
        return self.nome