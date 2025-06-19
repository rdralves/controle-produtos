from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.produto_list, name='produto_list'),
]
