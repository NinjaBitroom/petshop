from django.db import models
from stdimage import StdImageField


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Especie(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao


class Animal(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Macho'), ('F', 'Fêmea')])
    foto = StdImageField(upload_to='animal', variations={'thumb': {'width': 600, 'height': 600, 'crop': True}})
    idEspecie = models.ForeignKey(Especie, models.SET_NULL, null=True, blank=True)
    idCliente = models.ForeignKey(Cliente, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
