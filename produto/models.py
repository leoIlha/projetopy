from django.db import models

#conecta com bd tem insert....

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False, unique=True)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


