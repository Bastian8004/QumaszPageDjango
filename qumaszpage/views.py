from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def main(request):
    return render(request, 'main.html')

def uslugi(request):
    return render(request, 'uslugi.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def cennik(request):
    return render(request, 'cennik.html')

def conowego(request):
    return render(request, 'conowego.html')

def onas(request):
    return render(request, 'onas.html')

def opinie(request):
    return render(request, 'opinie.html')