from django.shortcuts import render

def index(request):
    context ={
            "nome": "Gabriel"
    }
    return render(request, 'conteudo.html', context)