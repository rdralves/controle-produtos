from django.contrib import admin
from .models import Produto
# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('ref_produto', 'descricao',
                    'quantidade', 'valor', 'data_entrada')
    search_fields = ('ref_produto', 'descricao')
