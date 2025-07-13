from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_hospedes, name='listar_hospedes'),
    path('novo/', views.cadastrar_hospede, name='cadastrar_hospede'),
    path('editar/<int:id>/', views.editar_hospede, name='editar_hospede'),
    path('deletar/<int:id>/', views.deletar_hospede, name='deletar_hospede'),
]