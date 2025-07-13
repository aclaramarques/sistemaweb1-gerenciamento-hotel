from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_quartos, name='listar_quartos'),
    path('novo/', views.cadastrar_quarto, name='cadastrar_quarto'),
    path('editar/<int:id>', views.editar_quarto, name='editar_quarto'),
    path('deletar/<int:id>', views.deletar_quarto, name='deletar_quarto'),
]