from tkinter import *

import sqlite3 as sq3

# *** Colores ***
boton_bg = 'grey25'
boton_fg = 'azure'


# *** Función listar alumnos ***
def listar_alumnos():

    # Clase Tabla
    class Tabla():

        def __init__(self, raiz2):
            nombre_columnas = ['Legajo', 'Alumno', 'Calificación', 'Email',
                               'Escuela', 'Localidad', 'Provincia']
            # Primera fila con los nombres de las columnas
            for i in range(cant_cols):
                self.e = Entry(frame_tabla)
                self.e.grid(row=0, column=i)
                self.e.config(readonlybackground=boton_bg, fg=boton_fg)
                self.e.insert(END, nombre_columnas[i])
                self.e.config(state='readonly')
            # Dos bucles for anidados para completar la tabla
            for f in range(cant_filas):
                for c in range(cant_cols):
                    self.e = Entry(frame_tabla)
                    self.e.grid(row=f+1, column=c)
                    self.e.insert(END, datos[f][c])
                    self.e.config(state='readonly')

    # Creación de la ventana
    raiz2 = Tk()
    raiz2.title('Listado de alumnos')
    frame_tabla = Frame(raiz2)
    frame_tabla.pack(fill='both')
    frame_cerrar = Frame(raiz2)
    frame_cerrar.pack(fill='both')
    cerrar_btn = Button(frame_cerrar, text='Cerrar', command=raiz2.destroy)
    cerrar_btn.config(bg=boton_bg, fg=boton_fg)
    cerrar_btn.pack(fill='both')

    # Obtención de datos
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    query = '''
    SELECT alumnos.legajo, alumnos.nombre, alumnos.nota, 
    alumnos.email, escuelas.nombre, escuelas.localidad, escuelas.provincia 
    FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id
    '''
    cur.execute(query)
    datos = cur.fetchall()
    cant_filas = len(datos)  # Cantidad de registros, para saber cuántas filas
    cant_cols = len(datos[0])  # Cantidad de columnas

    tabla = Tabla(frame_tabla)

    con.close()
    raiz2.mainloop()
