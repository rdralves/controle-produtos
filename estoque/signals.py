from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movimentacao


@receiver(post_save, sender=Movimentacao)
def atualizar_saldo_produto(sender, instance, created, **kwargs):
    if created:
        produto = instance.produto
        if instance.tipo == 'E':
            produto.quantidade += instance.quantidade
        elif instance.tipo == 'S':
            produto.quantidade -= instance.quantidade
            if produto.quantidade < 0:
                produto.quantidade = 0  # Evita saldo negativo
        produto.save()
