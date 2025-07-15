from django.urls import path
from . import views

urlpatterns = [
    path('reservas', views.listar_reservas, name='listar_reservas'),
    path('nova-reserva/', views.cadastrar_reserva, name='cadastrar_reserva'),
    path('editar-reserva/<int:id>', views.editar_reserva, name='editar_reserva'),
    path('deletar-reserva/<int:id>', views.deletar_reserva, name='deletar_reserva'),
]