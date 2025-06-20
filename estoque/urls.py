from .views import (
    ExportarProdutosExcelView, ProdutoListView, ProdutoDetailView, ProdutoCreateView,
    ProdutoUpdateView, ProdutoDeleteView, RelatorioProdutosView
)
from django.urls import path
from . import views
from .views import RelatorioProdutosView, ExportarProdutosExcelView

urlpatterns = [
    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/',
         ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/excluir/',
         ProdutoDeleteView.as_view(), name='produto_delete'),
    path('relatorios/produtos/', RelatorioProdutosView.as_view(),
         name='relatorio_produtos'),
    path('relatorios/produtos/exportar/',
         ExportarProdutosExcelView.as_view(), name='exportar_produtos_excel'),
]
