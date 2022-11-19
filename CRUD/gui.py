from tkinter import *

from crud import conectar, salir, buscar_escuelas, limpiar_campos
from crud import mostrar_licencia, mostrar_acercade
from crud import buscar_legajo, crear, actualizar, borrar

from listar import listar_alumnos

"""
************************
*   Interfaz gráfica   *
************************
"""

# *** Colores ***

# Colores frame botones
frame_botones_bg = 'grey19'
boton_bg = 'grey25'
boton_fg = 'azure'

# Colores frame campos
frame_campos_bg = 'grey29'
label_fg = 'AntiqueWhite1'

# Colores frame pie
frame_copy_bg = frame_campos_bg


# *** Raíz ***
raiz = Tk()
raiz.title('Python CRUD - Big Data c22610')


# *** Barra menú ***
barra_menu = Menu(raiz)
raiz.config(menu=barra_menu)

bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label='Conectar', command=conectar)
bbdd_menu.add_command(label='Listado alumnos', command=listar_alumnos)
bbdd_menu.add_separator()
bbdd_menu.add_command(label='Salir', command=salir)

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label='Limpiar campos', command=limpiar_campos)

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label='Licencia', command=mostrar_licencia)
ayuda_menu.add_command(label='Acerca de...', command=mostrar_acercade)

barra_menu.add_cascade(label='BBDD', menu=bbdd_menu)
barra_menu.add_cascade(label='Limpiar', menu=borrar_menu)
barra_menu.add_cascade(label='Acerca de', menu=ayuda_menu)


# *** Frame para los campos ***
frame_campos = Frame(raiz)
frame_campos.config(bg=frame_campos_bg)
frame_campos.pack(fill='both')

# Variables para los campos
legajo = StringVar()
alumno = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

# Entry
legajo_input = Entry(frame_campos, textvariable=legajo, width=35)
legajo_input.grid(row=0, column=1, padx=10, pady=10)

alumno_input = Entry(frame_campos, textvariable=alumno, width=35)
alumno_input.grid(row=1, column=1, padx=10, pady=10)

email_input = Entry(frame_campos, textvariable=email, width=35)
email_input.grid(row=2, column=1, padx=10, pady=10)

calificacion_input = Entry(frame_campos, textvariable=calificacion, width=35)
calificacion_input.grid(row=3, column=1, padx=10, pady=10)

lista_escuelas = buscar_escuelas(False)
escuela.set('- Seleccione -')
escuela_option = OptionMenu(frame_campos, escuela, *lista_escuelas)
escuela_option.grid(row=4, column=1, padx=10, pady=10, sticky=W+E)
# escuela_input = Entry(frame_campos, textvariable=escuela)
# escuela_input.grid(row=4, column=1, padx=10, pady=10)

localidad_input = Entry(frame_campos, textvariable=localidad, width=35)
localidad_input.grid(row=5, column=1, padx=10, pady=10)
localidad_input.config(state='readonly')

provincia_input = Entry(frame_campos, textvariable=provincia, width=35)
provincia_input.grid(row=6, column=1, padx=10, pady=10)
provincia_input.config(state='readonly')


# Label
def config_label(mi_label, fila):
    ubicacion = {'column': 0, 'sticky': 'e', 'padx': 10, 'pady': 10}
    colores = {'bg': frame_campos_bg, 'fg': label_fg}

    mi_label.grid(row=fila, **ubicacion)
    mi_label.config(**colores)


legajo_label = Label(frame_campos, text='Legajo:')
config_label(legajo_label, 0)

alumno_label = Label(frame_campos, text='Alumno:')
config_label(alumno_label, 1)

email_label = Label(frame_campos, text='Email:')
config_label(email_label, 2)

calificacion_label = Label(frame_campos, text='Calificación:')
config_label(calificacion_label, 3)

escuela_label = Label(frame_campos, text='Escuela:')
config_label(escuela_label, 4)

localidad_label = Label(frame_campos, text='Localidad:')
config_label(localidad_label, 5)

provincia_label = Label(frame_campos, text='Provincia:')
config_label(provincia_label, 6)


# *** Frame botonera ***
frame_botones = Frame(raiz)
frame_botones.config(bg=frame_botones_bg)
frame_botones.pack()

# Botones
crear_btn = Button(frame_botones, text='Crear', width=9, command=crear)
crear_btn.grid(row=0, column=0, padx=5, pady=10)
crear_btn.config(bg=boton_bg, fg=boton_fg)

leer_btn = Button(frame_botones, text='Leer', width=9, command=buscar_legajo)
leer_btn.grid(row=0, column=1, padx=5, pady=10)
leer_btn.config(bg=boton_bg, fg=boton_fg)

actualizar_btn = Button(frame_botones, text='Actualizar',
                        width=9, command=actualizar)
actualizar_btn.grid(row=0, column=2, padx=5, pady=10)
actualizar_btn.config(bg=boton_bg, fg=boton_fg)

borrar_btn = Button(frame_botones, text='Borrar', width=9, command=borrar)
borrar_btn.grid(row=0, column=3, padx=5, pady=10)
borrar_btn.config(bg=boton_bg, fg=boton_fg)


# *** Frame pie ***
frame_copy = Frame(raiz)
frame_copy.config(bg=frame_copy_bg)
frame_copy.pack(fill='both')

copy_msg = '(2022) por Pablo Godoy para CaC 4.0 - Big Data'
copy_label = Label(frame_copy, text=copy_msg)
copy_label.config(bg=frame_copy_bg, fg=label_fg)
copy_label.pack(side='right')


# Última linea del programa GUI
raiz.mainloop()
