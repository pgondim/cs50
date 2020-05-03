from django.contrib import admin

from .models import Aeroporto, Voo, Passageiros
# Register your models here.

admin.site.register(Aeroporto)
admin.site.register(Voo)
admin.site.register(Passageiros)
