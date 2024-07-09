from django.shortcuts import render
from .models import register

def signup (request):
    if request.method == 'POST':
        print("Probando")
        print(request.POST)
        print(request.POST["nombre"])
            
        user = register.objects.create (
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
            email = request.POST["email"],
            password = request.POST["password"],
        )
        user.save()
        return render(request, 'signup.html')
    else:
        print("Estas en el ELSE")
        return render(request, 'signup.html')
