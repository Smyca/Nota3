from django.shortcuts import render
from .models import Registro

def registroView(request):
    if request.method == 'POST':
        nombre      = request.POST.get("nombre", "").strip()
        apellido    = request.POST.get("apellido", "").strip()
        email       = request.POST.get("email", "").strip()
        password    = request.POST.get("password", "").strip()

        # Validar si alguno de los campos está vacío
        if not nombre or not apellido or not email or not password:
            error_message = "Todos los campos son obligatorios."
            return render(request, 'registro.html', {'error_message': error_message})
        else:
            # Crear y guardar el usuario si todos los campos están completos
            user = Registro.objects.create(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=password
            )
            user.save()
            success_message = "Registro exitoso."
            return render(request, 'registro.html', {'success_message': success_message})
    else:
        print("Estas en el ELSE")
        return render(request, 'registro.html')
