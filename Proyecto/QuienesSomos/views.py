from django.shortcuts import render

# Create your views here.
def quienesSomosView(request):
    return render(request,'QuienesSomos.html')