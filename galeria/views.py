from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from galeria.models import Fotografia
from django.contrib import messages
from galeria.forms import FotografiaForm

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('usuarios:login')
    
    fotografias = Fotografia.objects.filter(publicada=True)
    return render(request,'galeria/index.html', {'cards': fotografias})

def imagem(request, fotografia_id):
    fotografia = get_object_or_404(Fotografia, pk=fotografia_id)
    return render(request,'galeria/imagem.html', {'card': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('usuarios:login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar: 
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render (request, "galeria/buscar.html", {"cards": fotografias})

def nova_imagem(request):
    form = FotografiaForm
    return render(request,'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass