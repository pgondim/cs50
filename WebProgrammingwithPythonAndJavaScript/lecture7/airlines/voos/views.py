from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Voo, Passageiros


# Create your views here.
def index(request):
    context = {
        "voos": Voo.objects.all()
    }
    return render(request, "voos/index.html", context)


def voo(request, voo_id):
    try:
        voo = Voo.objects.get(pk = voo_id)
    except Voo.DoesNotExist:
        raise Http404("Voo não existe.")

    context = {
        "voo": voo,
        "passageiros": voo.passageiros.all(),
        "nao_passageiros": Passageiros.objects.exclude(voos=voo).all(),

    }
    return render(request, "voos/voo.html", context)

def comprar(request, voo_id):
    try:
        passageiro_id = int(request.POST["passageiro"])
        passageiro = Passageiros.objects.get(pk = passageiro_id)
        voo = Voo.objects.get(pk = voo_id)
    except KeyError:
        return render(request, "voos/error.html", {"mensagem": "Passageiro não selecionado."})
    except Passageiros.DoesNotExist:
        return render(request, "voos/error.html", {"mensagem": "Cadastre o passaeiro antes."})
    except Voo.DoesNotExist:
        return render(request, "voos/error.html", {"mensagem": "Esse voo não existe"})
    
    passageiro.voos.add(voo)
    return HttpResponseRedirect(reverse("voo", args=[voo_id]))
    


