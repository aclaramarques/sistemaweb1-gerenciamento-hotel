from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tudo, name='listar_tudo'),
]