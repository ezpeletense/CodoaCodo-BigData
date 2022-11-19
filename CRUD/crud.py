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
def mostrar_licencia():
    # CREATIVE COMMONS GNU GPL https://www.gnu.org/licenses/gpl-3.0.txt
    gnugpl = '''
    Sistema CRUD en Python
    Copyright (C) 2022 - Pablo Godoy
    Email: Ezpeletense@gmail.com
    ============================
    This program is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public 
    License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any 
    later version.
    This program is distributed in the hope that it will be 
    useful, but WITHOUT ANY WARRANTY; without even the 
    implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE.  See the GNU General Public License 
    for more details.
    You should have received a copy of the GNU General Public 
    License along with this program.  
    If not, see <https://www.gnu.org/licenses/>.
    '''
    messagebox.showinfo('Licencia', gnugpl)


def mostrar_acercade():
    msg = '''
    Creado por Pablo Godoy
    para Codo a Codo 4.0 - Big Data
    Noviembre 2022
    Email: ezpeletense@gmail.com'''
    messagebox.showinfo('Acerca de', msg)


# *** Funciones CRUD ***

# ** Crear **
def crear():
    id_escuela = int(buscar_escuelas(True)[0])
    datos = (id_escuela, gui.legajo.get(), gui.alumno.get(),
             gui.calificacion.get(), gui.email.get(),)
    query = '''INSERT INTO alumnos (id_escuela, legajo, nombre, nota,
            email)VALUES (?, ?, ?, ?, ?)
            '''
    cur.execute(query, datos)
    con.commit()
    messagebox.showinfo('Status', '¡Registro creado con éxito!')
    limpiar_campos()


# ** Leer **
def buscar_legajo():
    query = '''SELECT alumnos.legajo, alumnos.nombre, alumnos.nota,
    alumnos.email, escuelas.nombre, escuelas.localidad, escuelas.provincia
    FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id
    WHERE alumnos.legajo =
    '''
    cur.execute(query + gui.legajo.get())
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
def actualizar():
    id_escuela = int(buscar_escuelas(True)[0])
    datos = (id_escuela, gui.alumno.get(), gui.calificacion.get(),
             gui.email.get(),)
    query = '''UPDATE alumnos SET id_escuela = ?, nombre = ?, nota = ?, 
            email = ? WHERE legajo = ''' + gui.legajo.get()
    cur.execute(query, datos)
    con.commit()
    messagebox.showinfo('Status', '¡Registro modificado con éxito!')
    limpiar_campos()


# ** Borrar **
def borrar():
    respuesta = messagebox.askquestion('Borrar', '¿Desea borrar el registro?')
    if respuesta == 'yes':
        cur.execute('DELETE FROM alumnos WHERE legajo = ' + gui.legajo.get())
        con.commit()
        messagebox.showinfo('Status', 'El registro fue eliminado')
        limpiar_campos()


# *** Otras funciones ***

# Buscar escuelas
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
        if actualiza:
            gui.localidad.set(e[1])
            gui.provincia.set(e[2])
        esc = e[0]
        retorno.append(esc)

    con.close()
    return retorno
