from django.shortcuts import render
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        usuarios = {
            "correo@correo.com": "12345",
            "nicol@correo.com": "54321",
            "carlos@correo.com": "55555"
        }
        if correo in usuarios and usuarios[correo] == contrasena:
            messages.success(request, f"Bienvenido {correo}")
            return render(request, 'usuarios/bienvenido.html', {'usuario': correo})
        else:
            messages.error(request, "Correo o contraseña incorrectos.")
    return render(request, 'usuarios/login.html')


def bienvenido_view(request):
    return render(request, 'usuarios/bienvenido.html')
