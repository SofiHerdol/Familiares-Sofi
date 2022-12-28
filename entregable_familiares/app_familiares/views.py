

from django.shortcuts import render
from django.http import HttpResponse
from app_familiares.models import Familiares

def create_familiar(request):
    new_familiar = Familiares.objects.create(name = "Familiar sin desbloquear", age = 0, alive = True)
    print(new_familiar)
    return render(request, "create_familiar.html", context={})

def family_list(request):
    all_family = Familiares.objects.all()
    print(all_family)
    context = {
        "family":all_family,
    }
    return render(request, "family_list.html", context=context)

def saludo_inicio(request):
    return render(request, "index.html", context={})