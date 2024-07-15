from django.shortcuts import render

# Create your views here.
def mapaView(request):
    return render(request,'mapa.html')