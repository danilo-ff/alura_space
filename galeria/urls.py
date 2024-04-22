from django.urls import path
from . import views

app_name = "galeria"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fotografia_id>/', views.imagem, name='imagem'),
    path("buscar", views.buscar, name="buscar"),
    path("nova-imagem", views.nova_imagem, name="nova_imagem"),
    path("editar-imagem", views.editar_imagem, name="editar_imagem"),
    path("deletar-imagem", views.deletar_imagem, name="deletar_imagem"),
]