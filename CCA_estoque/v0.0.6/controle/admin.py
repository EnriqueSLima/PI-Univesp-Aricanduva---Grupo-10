from django.contrib import admin
from .models import Tipo, Genero, Core, Tamanho, Uniforme

admin.site.register(Tipo)
admin.site.register(Genero)
admin.site.register(Core)
admin.site.register(Tamanho)
admin.site.register(Uniforme)

