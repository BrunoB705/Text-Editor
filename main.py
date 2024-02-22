from tkinter import *
import tkinter as tk
from tkinter import filedialog as FileDialog, messagebox
from io import open


route = ''
def nuevoFunc():
    global route
    route = ''
    texto.delete('1.0',"end-1c")
    root.title("Editor de texto")

def abrirFunc():
    global route
    route = FileDialog.askopenfilename(initialdir='.', filetypes=(('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')), title="Abrir un archivo de texto")
    if route:
        fichero = open(route,'r')
        contenido = fichero.read()
        texto.delete('1.0',"end-1c")
        texto.insert('insert',contenido)
        fichero.close()
        root.title(route + '- Editor de Texto')

def guardarFunc():
    global route
    if route !="":
        contenido = texto.get('1.0',"end-1c")
        fichero = open(route,'w+')
        fichero.write(contenido)
        fichero.close()
    else:
        guardarcomoFunc()

def guardarcomoFunc():
    global route
    route = FileDialog.asksaveasfilename(title="Guardar texto", defaultextension='.txt')
    if route:
        guardarFunc()
    else:
        route = ''

def buscartextoFunc():
    ventana_busqueda = tk.Toplevel(root)
    ventana_busqueda.title("Buscar")

    def buscar_palabra(event=None):
        palabra = entrada_palabra.get()
        if palabra:

            texto.tag_remove("found", "1.0", "end")

            inicio = "1.0"
            while True:
                inicio = texto.search(palabra, inicio, stopindex="end")
                if not inicio:
                    break
                fin = f"{inicio}+{len(palabra)}c"
                texto.tag_add("found", inicio, fin)
                inicio = fin

            texto.tag_configure("found", background="#ADD8E6")

            ventana_busqueda.after(2000, lambda: texto.tag_configure("found", background=""))
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una palabra para buscar.")


    etiqueta_palabra = tk.Label(ventana_busqueda, text="Palabra a buscar:")
    etiqueta_palabra.pack()

    entrada_palabra = tk.Entry(ventana_busqueda)
    entrada_palabra.pack()
    entrada_palabra.bind("<Return>", buscar_palabra)

root = Tk()
root.geometry("800x600")
root.title("Editor de Texto")

menuBar = Menu(root)


filemenu = Menu(type="menubar",tearoff=0)
menuBar.add_cascade(menu=filemenu,label="Archivo")
filemenu.add_command(label="Nuevo",command=nuevoFunc)
filemenu.add_command(label="Abrir",command=abrirFunc)
filemenu.add_command(label="Guardar",command=guardarFunc)
filemenu.add_command(label="Guardar como",command=guardarcomoFunc)
filemenu.add_command(label="Salir",command=root.quit)

optionm = Menu(type="normal",tearoff=0)
menuBar.add_cascade(menu=optionm,label="Opciones")
optionm.add_command(label="Buscar",command=buscartextoFunc)

texto = Text(root)
texto.pack(fill="both",expand=True)
texto.config(padx=3,pady=3,font=("Arial",12))

mensaje = StringVar()
mensaje.set("Editor de texto")
monitor = Label(root,textvariable=mensaje,justify="left")
monitor.pack(side="left")

root.config(menu=menuBar)
root.mainloop()
