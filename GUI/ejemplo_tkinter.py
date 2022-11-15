from tkinter import *

"""
************************
*   Interfaz gráfica   *
************************
"""

# *** Raíz ***
raiz = Tk()
raiz.title('Python CRUD - Big Data c22610')


# *** Barra menú ***
barra_menu = Menu(raiz)
raiz.config(menu=barra_menu)

bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label='Conectar')
bbdd_menu.add_command(label='Salir')

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label='Limpiar campos')

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label='Licencia')
ayuda_menu.add_command(label='Acerca de...')

barra_menu.add_cascade(label='BBDD', menu=bbdd_menu)
barra_menu.add_cascade(label='Limpiar', menu=borrar_menu)
barra_menu.add_cascade(label='Acerca de', menu=ayuda_menu)


# *** Frame para los campos ***
frame_campos = Frame(raiz)
frame_campos.pack()

# Variables para los campos
legajo = StringVar()
alumno = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

# Entry
legajo_input = Entry(frame_campos, textvariable=legajo)
legajo_input.grid(row=0, column=1, padx=10, pady=10)

alumno_input = Entry(frame_campos, textvariable=alumno)
alumno_input.grid(row=1, column=1, padx=10, pady=10)

email_input = Entry(frame_campos, textvariable=email)
email_input.grid(row=2, column=1, padx=10, pady=10)

calificacion_input = Entry(frame_campos, textvariable=calificacion)
calificacion_input.grid(row=3, column=1, padx=10, pady=10)

escuela_input = Entry(frame_campos, textvariable=escuela)
escuela_input.grid(row=4, column=1, padx=10, pady=10)

localidad_input = Entry(frame_campos, textvariable=localidad)
localidad_input.grid(row=5, column=1, padx=10, pady=10)

provincia_input = Entry(frame_campos, textvariable=provincia)
provincia_input.grid(row=6, column=1, padx=10, pady=10)

# Label
legajo_label = Label(frame_campos, text='Legajo:')
legajo_label.grid(row=0, column=0, sticky='e', padx=10, pady=10)

alumno_label = Label(frame_campos, text='Alumno:')
alumno_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)

email_label = Label(frame_campos, text='Email:')
email_label.grid(row=2, column=0, sticky='e', padx=10, pady=10)

calificacion_label = Label(frame_campos, text='Calificación:')
calificacion_label.grid(row=3, column=0, sticky='e', padx=10, pady=10)

escuela_label = Label(frame_campos, text='Escuela:')
escuela_label.grid(row=4, column=0, sticky='e', padx=10, pady=10)

localidad_label = Label(frame_campos, text='Localidad:')
localidad_label.grid(row=5, column=0, sticky='e', padx=10, pady=10)

provincia_label = Label(frame_campos, text='Provincia:')
provincia_label.grid(row=6, column=0, sticky='e', padx=10, pady=10)


# *** Frame botonera ***
frame_botones = Frame(raiz)
frame_botones.pack()

# Botones
crear_btn = Button(frame_botones, text='Crear')
crear_btn.grid(row=0, column=0, padx=5, pady=10)

leer_btn = Button(frame_botones, text='Leer')
leer_btn.grid(row=0, column=1, padx=5, pady=10)

actualizar_btn = Button(frame_botones, text='Actualizar')
actualizar_btn.grid(row=0, column=2, padx=5, pady=10)

borrar_btn = Button(frame_botones, text='Borrar')
borrar_btn.grid(row=0, column=3, padx=5, pady=10)


# *** Frame pie ***
frame_copy = Frame(raiz)
frame_copy.pack()

copy_msg = '(2022) por Pablo Godoy para CaC 4.0 - Big Data'
copy_label = Label(frame_copy, text=copy_msg)
copy_label.grid(row=0, column=0, padx=10, pady=5)


# Última linea del programa GUI
raiz.mainloop()
