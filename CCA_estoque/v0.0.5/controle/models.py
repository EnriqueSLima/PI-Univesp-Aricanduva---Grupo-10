from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

class Estilo(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)
    estilo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.estilo}"

class Core(models.Model):
    cor = models.CharField(max_length=20)

    def __str__(self):
        return self.cor

class Tamanho(models.Model):
    tamanho = models.CharField(max_length=3)

    def __str__(self):
        return self.tamanho

class Uniforme(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)
    estilo = models.ForeignKey(Estilo, on_delete=models.DO_NOTHING)
    cor = models.ForeignKey(Core, on_delete=models.DO_NOTHING)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.DO_NOTHING)
    qtd = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.tipo} - {self.estilo} - {self.cor} - tamanho: {self.tamanho} - quantidade: {self.qtd}"

