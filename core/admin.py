from django.contrib import admin
from core.models import Cliente, Animal, Especie


# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'bairro', 'cep', 'cidade', 'estado', 'telefone')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'foto', 'idEspecie', 'idCliente')


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
