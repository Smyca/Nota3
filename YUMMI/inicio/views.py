from django.shortcuts import render

def inicio_pagina(request):
    return render(request, 'home.html')