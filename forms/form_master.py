import tkinter as tk
from tkinter import Menu, Entry, Button, Label, Tk  # Importar los widgets necesarios de tkinter
from tkinter.font import BOLD  # Importar la opción de negrita para los textos
import util.generic as utl  # Importar utilidades como la carga de imágenes
 
# Definir las funciones para las operaciones de la calculadora
def fnSuma():
    """
    Realiza la suma de dos números obtenidos de los campos de entrada
    y muestra el resultado en el campo de salida.
    """
    n1 = txt1.get()  # Obtener el valor del primer campo de texto como cadena
    n2 = txt2.get()  # Obtener el valor del segundo campo de texto como cadena
    r = float(n1) + float(n2)  # Convertir las cadenas a números flotantes y sumar
    txt3.delete(0, 'end')  # Limpiar el campo de resultado
    txt3.insert(0, r)  # Insertar el resultado en el campo de resultado
 
def fnResta():
    """
    Realiza la resta de dos números obtenidos de los campos de entrada
    y muestra el resultado en el campo de salida.
    """
    n1 = txt1.get()  # Obtener el valor del primer campo de texto como cadena
    n2 = txt2.get()  # Obtener el valor del segundo campo de texto como cadena
    r = float(n1) - float(n2)  # Convertir las cadenas a números flotantes y restar
    txt3.delete(0, 'end')  # Limpiar el campo de resultado
    txt3.insert(0, r)  # Insertar el resultado en el campo de resultado
 
class PanelPrincipal:
    """
    Clase que crea la interfaz gráfica principal para la calculadora.
    """
 
    def __init__(self):
        """
        Inicializa la ventana principal y sus componentes.
        """
        self.ventana = Tk()  # Crear una instancia de la ventana principal
        self.ventana.title("Panel Principal con Calculadora")  # Establecer el título de la ventana
       
        # Obtener dimensiones de la pantalla y ajustar ventana
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()  # Obtener el ancho y alto de la pantalla
        self.ventana.geometry(f"{w}x{h}+0+0")  # Ajustar tamaño de la ventana al tamaño de la pantalla
        self.ventana.config(bg='#fcfcfc')  # Establecer el color de fondo de la ventana
        self.ventana.resizable(width=0, height=0)  # Evitar que la ventana se redimensione
       
        # Cargar el logo
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))  # Cargar la imagen del logo redimensionada
        label_logo = Label(self.ventana, image=logo, bg='#3a7ff6')  # Crear una etiqueta para mostrar el logo
        label_logo.place(x=0, y=0, relwidth=1, relheight=0.4)  # Ubicar el logo en la parte superior de la ventana
       
        # Crear menú
        self.crear_menu()  # Llamar al método para crear el menú
       
        # Crear los elementos de la interfaz de usuario (calculadora)
        global txt1, txt2, txt3  # Declarar los campos de texto globales para las operaciones
       
        # Campo de texto para el primer número
        txt1 = Entry(self.ventana)  # Crear un campo de entrada para el primer número
        lbl1 = Label(self.ventana, text="Primer número", font=("Arial", 12), bg='#fcfcfc')  # Etiqueta para el primer número
        lbl1.place(relx=0.5, rely=0.5, anchor='center')  # Ubicar la etiqueta en el centro de la ventana
        txt1.place(relx=0.5, rely=0.55, anchor='center')  # Ubicar el campo de entrada debajo de la etiqueta
       
        # Campo de texto para el segundo número
        txt2 = Entry(self.ventana)  # Crear un campo de entrada para el segundo número
        lbl2 = Label(self.ventana, text="Segundo número", font=("Arial", 12), bg='#fcfcfc')  # Etiqueta para el segundo número
        lbl2.place(relx=0.5, rely=0.6, anchor='center')  # Ubicar la etiqueta en el centro de la ventana
        txt2.place(relx=0.5, rely=0.65, anchor='center')  # Ubicar el campo de entrada debajo de la etiqueta
       
        # Campo de texto para el resultado
        txt3 = Entry(self.ventana)  # Crear un campo de entrada para mostrar el resultado
        lbl3 = Label(self.ventana, text="Resultado", font=("Arial", 12), bg='#fcfcfc')  # Etiqueta para el resultado
        lbl3.place(relx=0.5, rely=0.7, anchor='center')  # Ubicar la etiqueta en el centro de la ventana
        txt3.place(relx=0.5, rely=0.75, anchor='center')  # Ubicar el campo de entrada debajo de la etiqueta
       
        # Botones de Sumar, Restar y Salir
        btn_sumar = Button(self.ventana, text="Sumar", command=fnSuma)  # Crear un botón para la suma
        btn_sumar.place(relx=0.4, rely=0.85, anchor='center')  # Ubicar el botón en la ventana
       
        btn_restar = Button(self.ventana, text="Restar", command=fnResta)  # Crear un botón para la resta
        btn_restar.place(relx=0.6, rely=0.85, anchor='center')  # Ubicar el botón en la ventana
       
        btn_salir = Button(self.ventana, text="Salir", command=self.fnSalir, bg="#E74C3C", fg="#FFF")  # Crear un botón para salir
        btn_salir.place(relx=0.5, rely=0.9, anchor='center')  # Ubicar el botón en la ventana
       
        # Iniciar el bucle principal de la interfaz gráfica
        self.ventana.mainloop()
   
    def crear_menu(self):
        """
        Crea el menú de la ventana principal.
        """
        barra_menu = Menu(self.ventana)  # Crear una barra de menú
        self.ventana.config(menu=barra_menu)  # Asignar la barra de menú a la ventana
       
        # Crear el menú "Inicio" con una opción "Salir"
        menu_inicio = Menu(barra_menu, tearoff=0)  # Crear un menú desplegable sin bordes
        barra_menu.add_cascade(label="Inicio", menu=menu_inicio)  # Añadir el menú "Inicio" a la barra de menú
        menu_inicio.add_command(label="Salir", command=self.fnSalir)  # Añadir la opción "Salir" al menú
       
        # Crear el menú "Operación" con opciones "Sumar" y "Restar"
        menu_operacion = Menu(barra_menu, tearoff=0)  # Crear un menú desplegable sin bordes
        barra_menu.add_cascade(label="Operación", menu=menu_operacion)  # Añadir el menú "Operación" a la barra de menú
        menu_operacion.add_command(label="Sumar", command=fnSuma)  # Añadir la opción "Sumar" al menú
        menu_operacion.add_command(label="Restar", command=fnResta)  # Añadir la opción "Restar" al menú
   
    def fnSalir(self):
        """
        Cierra la ventana principal.
        """
        self.ventana.destroy()  # Destruir la ventana principal para cerrar la aplicación
 
# Crear e iniciar la ventana principal
if __name__ == "__main__":
    app = PanelPrincipal()  # Crear una instancia de PanelPrincipal, que inicia la aplicación