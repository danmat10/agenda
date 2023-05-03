from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

from contatos.models import Contatos

# Create your views here.


def index(request):
    contatos = Contatos.objects.all()
    return render(request, 'pages/index.html', {'contatos': contatos})


def editar_contatos(request, contato_id):
    contato = Contatos.objects.get(id=contato_id)
    if request.method == 'POST':
        contato.nome = request.POST.get('nome')
        contato.cpf = request.POST.get('cpf')
        contato.email = request.POST.get('email')
        contato.telefone = request.POST.get('telefone')
        contato.altura = request.POST.get('altura')
        contato.descricao = request.POST.get('descricao')
        contato.data_nascimento = request.POST.get('data_nascimento')
        contato.ativo = request.POST.get('ativo') == 'on'
        contato.save()
        return HttpResponseRedirect("/contatos")

    data_nascimento = contato.data_nascimento.strftime('%Y-%m-%d')
    return render(request, 'pages/editar.html', {'contato': contato, 'data_nascimento': data_nascimento})


def redirect(request):
    return HttpResponseRedirect("contatos")
