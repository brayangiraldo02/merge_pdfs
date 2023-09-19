#pip install pypdf2
#Libreria para unir los pdfs
import PyPDF2

#Libreria para abrir el explorador de archivos
import tkinter as tk
from tkinter import filedialog

#Función para mostrar mensajes emergentes
def mostrar_mensaje(titulo, mensaje):
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title(titulo)
    mensaje_label = tk.Label(ventana_emergente, text=mensaje)
    mensaje_label.pack()
    ventana_emergente.after(3000, ventana_emergente.destroy)  # Cierra la ventana emergente después de 2.5 segundos

#Función para abrir el explorador de archivos
def abrir_explorador():
    archivos = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
    if len(archivos) < 2:
        mostrar_mensaje("ERROR", "Debes seleccionar al menos 2 archivos PDF.")
    if len(archivos) > 1:
        for archivo in archivos:
            print("Archivo seleccionado:", archivo)
        archivos_seleccionados.extend(archivos)
        mostrar_mensaje("ATENCIÓN", "Se han seleccionado los PDFs, puedes darle a unir.")
    
def unir_pdf(archivos_seleccionados):
    ruta_salida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
    if ruta_salida:
        pdf_final = PyPDF2.PdfMerger()
        for nombre_archivo in archivos_seleccionados:
            pdf_final.append(nombre_archivo)
        pdf_final.write(ruta_salida)
        pdf_final.close()

# Crear una ventana de tkinter
ventana = tk.Tk()
ventana.title("PDFs Manager")
ventana.geometry("300x100")  # Establecer el tamaño de la ventana (ancho x alto)

# Lista para almacenar los archivos seleccionados
archivos_seleccionados = []
 
# Botón para abrir el explorador de archivos
boton = tk.Button(ventana, text="Seleccionar archivos PDF", command=abrir_explorador)
boton.pack(pady=20)  # Añadir un espacio en blanco entre el botón y el siguiente

# Botón para unir los archivos PDF
boton_unir = tk.Button(ventana, text="Unir PDFs", command=lambda: unir_pdf(archivos_seleccionados))
boton_unir.pack()

#Ejecutar la ventana
ventana.mainloop()