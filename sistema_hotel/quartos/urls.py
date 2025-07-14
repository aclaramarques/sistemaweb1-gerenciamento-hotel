from django.urls import path
from . import views

urlpatterns = [
    path('quartos', views.listar_quartos, name='listar_quartos'),
    path('novo-quarto/', views.cadastrar_quarto, name='cadastrar_quarto'),
    path('editar-quarto/<int:id>', views.editar_quarto, name='editar_quarto'),
    path('deletar-quarto/<int:id>', views.deletar_quarto, name='deletar_quarto'),
]