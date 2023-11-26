from django.urls import path
from . import views

app_name = "galeria"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fotografia_id>/', views.imagem, name='imagem'),
    path("buscar", views.buscar, name="buscar"),
]