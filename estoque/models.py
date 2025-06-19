from django.db import models


class Produto(models.Model):
    ref_produto = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField(default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrada = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.ref_produto} - {self.descricao}"


class Movimentacao(models.Model):
    TIPO_MOVIMENTO = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
    )

    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name='movimentacoes')
    tipo = models.CharField(max_length=1, choices=TIPO_MOVIMENTO)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto.ref_produto} ({self.quantidade})"
