from django.db import models

# Create your models here.

class Aeroporto(models.Model):
    codigo = models.CharField(max_length = 3)
    cidade = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.cidade} ({self.codigo})"

#related_names serve para eu conseguir encontrar os voos dentro do objeto aeroporto, mesmo ele sendo criado dentro de voo
class Voo(models.Model):
    origem = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name="decolagem")
    destino = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name="aterrizagem")
    duracao = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origem} -> {self.destino} em {self.duracao} minutos"

class Passageiros(models.Model):
    pnome = models.CharField(max_length = 64)
    unome = models.CharField(max_length = 64)
    voos = models.ManyToManyField(Voo, blank = True, related_name="passageiros")

    def __str__(self):
        return f"{self.pnome} {self.unome}"