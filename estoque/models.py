from django.db import models


class Produto(models.Model):
    ref_produto = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField(default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrada = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.ref_produto} - {self.descricao}"
