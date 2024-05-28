from django.shortcuts import render

def index(request):
    return render (request,'usuarios/index.html')

def teste(request):
    return render (request,'usuarios/teste.html')