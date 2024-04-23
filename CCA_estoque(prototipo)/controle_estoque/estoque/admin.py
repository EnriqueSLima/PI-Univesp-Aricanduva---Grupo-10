from django.contrib import admin

from .models import Uniforme, Tamanho, Core, Tipo, Teste

admin.site.register(Uniforme)
admin.site.register(Tamanho)
admin.site.register(Core)
admin.site.register(Tipo)
admin.site.register(Teste)

