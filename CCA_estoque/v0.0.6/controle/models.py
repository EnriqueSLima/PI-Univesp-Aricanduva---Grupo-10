from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

class Core(models.Model):
    cor = models.CharField(max_length=20)

    def __str__(self):
        return self.cor

class Tamanho(models.Model):
    tamanho = models.CharField(max_length=3)

    def __str__(self):
        return self.tamanho

class Genero(models.Model):
    genero = models.CharField(max_length=2)

    def __str__(self):
        return self.genero

class Uniforme(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)
    cor = models.ForeignKey(Core, on_delete=models.DO_NOTHING)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.DO_NOTHING)
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)
    qtd = models.PositiveIntegerField()
    local = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.tipo} - {self.genero} - {self.cor} - tamanho: {self.tamanho} - quantidade: {self.qtd} - local {self.local}"

