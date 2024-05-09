from django.db import models

class Uniforme(models.Model):
    TIPO_CHOICES = [
        ('Camiseta', 'Camiseta'),
        ('Bermuda', 'Bermuda'),
        ('Calça', 'Calça'),
        ('Agasalho', 'Agasalho'),
        # Add more choices as needed
    ]

    ESTILO_CHOICES = [
        ('Manga Longa', 'Manga Longa'),
        ('Manga Curta', 'Manga Curta'),
        ('Regata', 'Regata'),
        ('Taktel', 'Taktel'),
        ('Ciclista', 'Ciclista'),
        ('Avulsa', 'Avulsa'),
        ('Bailarina', 'Bailarina'),
        ('Avulsa', 'Avulsa'),
        ('Jaquetão', 'Jaquetão'),

        # Add more choices as needed
    ]

    COR_CHOICES = [
        ('Branca', 'Branca'),
        ('Azul', 'Azul'),
      
        # Add more choices as needed
    ]

    TAMANHO_CHOICES = [
        ('2', '2'),
        ('4', '2'),
        ('6', '2'),
        ('8', '2'),
        ('10', '2'),
        ('12', '2'),
        ('14', '14'),
        ('16', '16'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
        ('EG', 'EG'),
        # Add more choices as needed
    ]

    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    estilo = models.CharField(max_length=100, choices=ESTILO_CHOICES)
    cor = models.CharField(max_length=100, choices=COR_CHOICES)
    tamanho = models.CharField(max_length=10, choices=TAMANHO_CHOICES)
    qtd = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.tipo} - {self.estilo} - {self.cor} - {self.tamanho} - {self.qtd}"
