from PIL import ImageTK, Image

# Función para cargar y ajustar el tamaño de una imagen
def leer_imagen(ruta, tamaño):
    """
    Esta función lee una imagen desde una ruta especificada, la redimensiona al tamaño indicado
    y la devuelve en un formato que tkinter puede usar (ImageTk.PhotoImage).
   
    Parámetros:
    ruta (str): La ruta de la imagen.
    tamaño (tuple): Un tuple que contiene el ancho y alto deseado para la imagen.
   
    Retorno:
    ImageTk.PhotoImage: La imagen redimensionada lista para ser utilizada en tkinter.
    """
    return ImageTk.PhotoImage(Image.open(ruta).resize(tamaño, Image.ADAPTIVE))
 
# Función para centrar una ventana en la pantalla
def centrar_ventana(ventana, ancho_aplicacion, largo_aplicacion):  
    """
    Esta función calcula las coordenadas necesarias para centrar una ventana en la pantalla
    y ajusta su geometría de acuerdo al tamaño proporcionado.
   
    Parámetros:
    ventana (tk.Tk): La ventana que se va a centrar.
    ancho_aplicacion (int): El ancho de la ventana.
    largo_aplicacion (int): El largo (alto) de la ventana.
   
    Retorno:
    None: Ajusta directamente la geometría de la ventana.
    """
    # Obtenemos las dimensiones de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    largo_pantalla = ventana.winfo_screenheight()
   
    # Calculamos la posición x e y para centrar la ventana
    x = int((ancho_pantalla / 2) - (ancho_aplicacion / 2))
    y = int((largo_pantalla / 2) - (largo_aplicacion / 2))
   
    # Ajustamos la geometría de la ventana para que se centre
    return ventana.geometry(f"{ancho_aplicacion}x{largo_aplicacion}+{x}+{y}")