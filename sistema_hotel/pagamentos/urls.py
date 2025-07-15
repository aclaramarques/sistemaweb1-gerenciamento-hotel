from django.urls import path
from . import views

urlpatterns = [
    path('pagamentos', views.listar_quartos, name='listar_pagamentos'),
    path('novo-pagamento/', views.cadastrar_quarto, name='cadastrar_pagamento'),
    path('editar-pagamento/<int:id>', views.editar_quarto, name='editar_pagamento'),
    path('deletar-pagamento/<int:id>', views.deletar_quarto, name='deletar_pagamento'),
]