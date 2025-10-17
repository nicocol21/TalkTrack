usuarios = {
    "correo@correo.com": "12345",
    "nicol@correo.com": "54321",
    "carlos@correo.com": "55555"
}


def iniciar_sesion(correo, contraseña):
    if correo in usuarios and usuarios[correo] == contraseña:
        return True 
    else:
        return False