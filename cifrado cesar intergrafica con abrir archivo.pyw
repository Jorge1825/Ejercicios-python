
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sys
import os
import tkinter as tk






def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)




root = tk.Tk()
root.title("Cifrado cesar")

image_path = resource_path("icono.ico")
image_path2 = resource_path("cesar.png")

root.iconbitmap(image_path)
# variables
varopcion = IntVar()
sino = IntVar()

Msg = ""

frame = Frame(root)
frame.pack()
frame.config(width="650", height="350", padx=80, pady=20)

cesarimg = PhotoImage(file=image_path2)


Label(frame, image=cesarimg).pack()

messagebox.showinfo("Cifrado Cesar", "Programa elaborado por Jorge")


Label(frame, text="\n\nSeleccione la operación que desea realizar:").pack()


def imprimir(Labe1, salt):

    if varopcion.get() == 0:
        Label5.config(text="Texto a codificar:")
        Labe1.config(text="Salto de texto para codificar:")
        Labe1.grid(row=5, column=0, sticky="e")
        salt.grid(row=5, column=1)


def vermensaje(Labe1, salt):
    if varopcion.get() == 2:
        Labe1.grid(row=5, column=0, sticky="e")
        salt.grid(row=5, column=1)
        Label5.config(text="Texto a descodificar:")
        Labe1.config(text="Salto de texto para descodificar:")


Radiobutton(frame, text="Codificar", variable=varopcion, value=0,
            command=lambda: imprimir(Labe1, salt)).pack()
Radiobutton(frame, text="Descodificar", variable=varopcion, value=2,
            command=lambda: vermensaje(Labe1, salt)).pack()


frame2 = Frame(frame)
frame2.pack()


def abrir():
    global Msg
    archivo = open(filedialog.askopenfilename(title="Abrir", initialdir="/",
                   filetypes=[("archivos de Texto", "*.txt")]), 'r', encoding="utf-8")
    Msg = archivo.read()

    lbl = Label(frame2, text="Archivo cargado", font=(
        "Comic Sans", 7))
    lbl.grid(row=0, column=2)


botr = Button(frame2, text="Abrir archivo", command=abrir)
botr.grid(row=0, column=1)


Label5 = Label(frame2, text="Texto a codificar:", font=("Comic Sans", 10))
Label5.grid(row=0, column=0, sticky="e")


label6 = Label(frame2, text="\n\n¡Desea utilizar una lista personalizada?", font=(
    "Comic Sans", 10))
label6.grid(row=1, column=0, columnspan=3, sticky="we", padx=10, pady=10)


def hide_button(B1, Lab):

    B1.grid_forget()
    Lab.grid_forget()


def show_button(B1, Lab):

    B1.grid(row=3, column=1)
    Lab.grid(row=3, column=0)


B1 = Text(frame2, width=16, height=3)
B1.grid_forget()
Lab = Label(frame2, text="Lista:", font=("Comic Sans", 10))
Lab.grid_forget()


r1 = Radiobutton(frame2, text="SI", variable=sino, value=1,
                 command=lambda: show_button(B1, Lab))
r2 = Radiobutton(frame2, text="NO", variable=sino, value=0,
                 command=lambda: hide_button(B1, Lab))
r1.grid(row=2, column=0, padx=50, pady=10)
r2.grid(row=2, column=1, padx=50, pady=10)


def validate_entry(text):
    return text.isdecimal()


Labe1 = Label(frame2, text="Salto de texto para codificar:",
              font=("Comic Sans", 10))

salt = Entry(frame2,
             validate="key",
             validatecommand=(root.register(validate_entry), "%S")
             )
Labe1.grid_forget()
salt.grid_forget()


Labe1.grid(row=5, column=0, sticky="e")
salt.grid(row=5, column=1)


frame3 = Frame(frame)
frame3.pack()


def por():
    global sino
    global varopcion
    global Msg

    if Msg == "":
        messagebox.showerror("Error", "No ha selecionado un archivo")

    else:

        msgc = ""

        if sino == 1:
            lista = B1.get("1.0", END)
 
        else:
            lista = "abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;()$%?¿!¡/+*-"

        if varopcion.get() == 0:
            try:
                salto = salt.get()
                salto = int(salto)
            except:
                messagebox.showerror(
                    "Error", "El salto debe ser un número entero")
                return
            for msg in Msg:  # Pasar cada letra del mensaje principal

                    if msg in lista:  # Buscar si la letra del mensaje principal está en la lista definida inicialmente
                        # Buscar posicion del elemento en la lista definida
                        Rempla = lista.find(msg)
                        Rempla += salto  # Asignar el nuevo numero de posicion
                        while True:
                            # Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                            if Rempla >= len(lista):
                                # A la nueva posición restarle la cantidad de elementos de la lista original
                                Rempla -= len(lista)
                                continue
                            else:
                                break

                        # Asignar a la lista msgc la nueva letra
                        msgc += lista[Rempla]
                    else:
                        # En caso de que el caracter no este definido en la lista original no se le hace cambios.
                        msgc += msg

            def guar(msgc):
                archivo_guardado = filedialog.asksaveasfilename(initialdir="/",
                                                                title="Seleccione archivo", defaultextension=".txt",
                                                                filetypes=(("Archivos txt", "*.txt"), ("Todos los archivos", "*.*")))

                encrip = open(archivo_guardado, "w", encoding="utf-8")
                encrip.truncate(0)
                encrip.write(msgc)
                encrip.close()
                raiz1.destroy()

            msgc = msgc.replace(" ", 'kl')
            msgc = msgc.replace("\n", 'jl')
            raiz1 = Tk()
            raiz1.title("Resultados")
            La = Label(raiz1, text="Resultados:", font=("Comic Sans", 14))
            La.pack()
            text = Text(raiz1, width=60)
            text.pack()
            fr = Frame(raiz1)
            fr.pack()
            btn = Button(fr, text="Salir", command=raiz1.destroy)
            btn.grid(row=0, column=2)

            lbl = Label(fr, text="")
            lbl.grid(row=0, column=1)

            btn1 = Button(fr, text="Guardar", command=lambda: guar(msgc))
            btn1.grid(row=0, column=1)

            text.insert(1.0, f"{msgc}")
            
            
            
            
            
            
            
            
            

        elif varopcion.get() == 2:

            try:
                salto = salt.get()
                salto = int(salto)
            except:
                messagebox.showerror(
                    "Error", "El salto debe ser un número entero")
                return
            
            Msg = Msg.replace("kl"," ")
            Msg = Msg.replace("jl",'\n')   
            print(Msg)
            
            for msg in Msg:  # Pasar cada letra del mensaje principal

                    if msg in lista:  # Buscar si la letra del mensaje principal está en la lista definida inicialmente
                        # Buscar posicion del elemento en la lista definida
                        Rempla = lista.find(msg)
                        Rempla -= salto  # Asignar el nuevo numero de posicion
                        # Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                        if Rempla >= len(lista):
                            # A la nueva posición restarle la cantidad de elementos de la lista original
                            Rempla -= len(lista)

                        while True:
                            if Rempla < 0:  # Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                Rempla += len(lista)
                                continue
                            else:
                                break

                        # Asignar a la lista msgc la nueva letra
                        msgc += lista[Rempla]
                    else:
                        # En caso de que el caracter no este definido en la lista original no se le hace cambios.
                        msgc += msg

                        
                        
            def guar(msgc):
                archivo_guardado = filedialog.asksaveasfilename(initialdir="/",
                                                                title="Seleccione archivo", defaultextension=".txt",
                                                                filetypes=(("Archivos txt", "*.txt"), ("Todos los archivos", "*.*")))

                encrip = open(archivo_guardado, "w", encoding="utf-8")
                encrip.truncate(0)
                encrip.write(msgc)
                encrip.close()
                raiz1.destroy()

            raiz1 = Tk()
            raiz1.title("Resultados")
            La = Label(raiz1, text="Resultados:", font=("Comic Sans", 14))
            La.pack()
            text = Text(raiz1, width=60)
            text.pack()
            fr = Frame(raiz1)
            fr.pack()
            btn = Button(fr, text="Salir", command=raiz1.destroy)
            btn.grid(row=0, column=2)

            lbl = Label(fr, text="")
            lbl.grid(row=0, column=1)

            btn1 = Button(fr, text="Guardar", command=lambda: guar(msgc))
            btn1.grid(row=0, column=1)

            text.insert(1.0, f"{msgc}")
            

Boton = Button(frame3, text="Generar texto", command=por)
Boton.pack()


root.mainloop()
