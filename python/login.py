import tkinter as tk

from tkinter import messagebox

from login import iniciar_sesion


def verificar_credenciales():

    correo = entry_correo.get()
    contrasena = entry_contrasena.get()

    acceso_valido = iniciar_sesion(correo, contrasena)

    if acceso_valido:
        messagebox.showinfo("Inicio de sesion")
    else:
        messagebox.showerror("Error coreo o contraseña incorrectos")

ventana = tk.Tk()

ventana.title("Login de usuario")

ventana.geometry("500x200")

tk.Label(ventana, text="correo electronico:").pack(pady=5)

entry_correo = tk.Entry(ventana, width=30)
entry_correo.pack()

tk.Label(ventana, text="Contraseña:").pack(pady=5)

entry_contrasena = tk.Entry(ventana, width=30, show="*")
entry_contrasena.pack()

tk.Button(ventana, text="Iniciar sesión", command=verificar_credenciales).pack(pady=15)

ventana.mainloop()