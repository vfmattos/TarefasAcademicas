from django.shortcuts import render
from .models import User

def index (requests):
        return render (requests,'account.html')

def user (requests):
        novo_usuario = User()
        novo_usuario.nome = requests.POST.get('name')
        novo_usuario.email = requests.POST.get('email')
        novo_usuario.save()

        usuarios = {
                'usuarios': User.objects.all()
        }
        return render(requests, 'user.html',usuarios)