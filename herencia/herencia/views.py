from django.shortcuts import render


def herencia(request):
    return render(request=request, template_name='herencia.html', context={})


def ejemploherencia(request):
    return render(request=request, template_name='ejemploherencia.html', context={})


def otra(request):
    return render(request=request, template_name='otra.html', context={})


def index(request):
    return render(request=request, template_name='index.html', context={})

