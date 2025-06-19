from .models import Produto, Movimentacao
from django.contrib import admin
from .models import Produto
# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('ref_produto', 'descricao',
                    'quantidade', 'valor', 'data_entrada')
    search_fields = ('ref_produto', 'descricao')


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data', 'observacao')
    list_filter = ('tipo', 'data', 'produto')
    search_fields = ('produto__ref_produto',
                     'produto__descricao', 'observacao')
