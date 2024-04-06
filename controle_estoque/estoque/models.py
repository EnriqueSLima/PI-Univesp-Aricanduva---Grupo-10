from django.db import models

class Tipo(models.Model):
    tipos = models.CharField(max_length = 20)
    def __str__(self):
        return self.tipos

class Tamanho(models.Model):
    tamanhos = models.CharField(max_length = 2)
    def __str__(self):
        return self.tamanhos

class Core(models.Model):
    cores = models.CharField(max_length = 20)
    def __str__(self):
        return self.cores

class Uniforme(models.Model):
    utipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    utamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    ucor = models.ForeignKey(Core, on_delete=models.CASCADE)
    uquantidade = models.IntegerField(default = 0)
    upreço = models.IntegerField(default = 0)
    def __str__(self):
        return (self.utipo, " | Tamanho ", self.utamanho," | Cor ", self.ucor," | Qtd ", self.uquantidade)
    