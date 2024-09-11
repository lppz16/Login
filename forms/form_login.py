import tkinter as tk
from tkinter import ttk, messagebox 
from tkinter.font import BOLD
import Util.generic as utl # Importa de la carpeta de utilidades
from form_master import PanelPrincipal

class App:

    def verificar(self):
        usuario=self.usuario.get()
        contrasena=self.password.get()

        if usuario == "salle" and contrasena =="12345":
            self.ventana.destroy()
            PanelPrincipal()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="ERROR")
    
    def __init__(self):        
        """
        Inicializa la ventana de inicio de sesión. Crea la estructura de la interfaz
        con campos de entrada para el usuario y la contraseña, además de un botón
        para iniciar sesión.
        """
        self.ventana = tk.Tk()  # Crea la ventana principal                      
        self.ventana.title('Inicio de sesión')  # Establece el título de la ventana
        self.ventana.geometry('800x500')  # Define el tamaño de la ventana
        self.ventana.config(bg='#fcfcfc')  # Configura el color de fondo
        self.ventana.resizable(width=0, height=0)  # Impide redimensionar la ventana
 
        # Centra la ventana en la pantalla
        utl.centrar_ventana(self.ventana, 800, 500)
 
        # Carga el logo desde un archivo
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
 
        # Crea el contenedor para el logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)  # Posiciona el frame a la izquierda
        label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')  # Crea una etiqueta para mostrar el logo
        label.place(x=0, y=0, relwidth=1, relheight=1)  # Coloca la imagen dentro del frame
 
        # Crea el contenedor para el formulario de inicio de sesión
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
 
        # Crea el encabezado del formulario
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesión", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
 
        # Crea el cuerpo del formulario
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
 
        # Etiqueta y campo de entrada para el usuario
        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))  # Campo de entrada para el usuario
        self.usuario.pack(fill=tk.X, padx=20, pady=10)
 
        # Etiqueta y campo de entrada para la contraseña
        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14), show="*")  # Campo de entrada para la contraseña (oculta con '*')
        self.password.pack(fill=tk.X, padx=20, pady=10)
 
        # Botón para iniciar sesión
        inicio = tk.Button(frame_form_fill, text="Iniciar sesión", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
 
        # Asocia la tecla 'Enter' con el método de verificación
        inicio.bind("<Return>", (lambda event: self.verificar()))
 
        # Ejecuta el ciclo principal de la ventana
        self.ventana.mainloop()
 
# Punto de entrada del programa
if __name__ == "__main__":
    App()  # Inicia la aplicación