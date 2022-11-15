from tkinter import *
from tkinter import messagebox

import sqlite3 as sq3
from asyncio.windows_events import NULL

import gui


"""
***********************
*   Parte funcional   *
***********************
"""

# *** Funciones barra menú ***

# ** BBDD **
# Conectar


def conectar():
    global con
    global cur
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    messagebox.showinfo('Status', '¡Conectado a la base de datos!')

# Salir


def salir():
    resp = messagebox.askquestion('Salir', '¿Desea salir de la aplicación?')
    if resp == 'yes':
        # con.close()
        gui.raiz.destroy()

# ** Limpiar **


def limpiar_campos():
    gui.legajo_input.config(state='normal')
    gui.legajo.set("")
    gui.alumno.set("")
    gui.calificacion.set("")
    gui.email.set("")
    gui.escuela.set('- Seleccione -')
    gui.localidad.set("")
    gui.provincia.set("")


# ** Acerca de **

# *** Funciones CRUD ***

# ** Crear **

# ** Leer **


def buscar_legajo():
    query_buscar = '''SELECT alumnos.legajo, alumnos.nombre, alumnos.nota,
    alumnos.email, escuelas.nombre, escuelas.localidad, escuelas.provincia
    FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id
    WHERE alumnos.legajo =
    '''
    cur.execute(query_buscar + gui.legajo.get())
    resultado = cur.fetchall()

    if not resultado:
        messagebox.showerror('Error', 'Ese n° de legajo no existe')
        gui.legajo.set("")
    else:
        for campo in resultado:
            gui.legajo.set(campo[0])
            gui.alumno.set(campo[1])
            gui.calificacion.set(campo[2])
            gui.email.set(campo[3])
            gui.escuela.set(campo[4])
            gui.localidad.set(campo[5])
            gui.provincia.set(campo[6])
            gui.legajo_input.config(state='disabled')

# ** Actualizar **

# ** Borrar **

# *** Otras funciones ***


def buscar_escuelas(actualiza):
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    if actualiza:
        # Ejecuta un query de los otros datos a partir de 'nombre'
        cur.execute(
            'SELECT _id, localidad, provincia FROM escuelas Where nombre = ?',
            (gui.escuela.get(),)
        )
    else:
        # Ejecuta un query de los nombres de las escuelas
        cur.execute('SELECT nombre FROM escuelas')

    resultado = cur.fetchall()
    retorno = []
    for e in resultado:
        # if actualiza:
        #     gui.localidad.set(e[1])
        #     gui.provincia.set(e[2])
        esc = e[0]
        retorno.append(esc)

    con.close()
    return retorno
