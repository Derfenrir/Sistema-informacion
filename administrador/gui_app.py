import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import time
import random
from itertools import cycle
from matplotlib.widgets import Button
import numpy as np
from tkinter import messagebox, filedialog
from tkinter import ttk, Scrollbar, HORIZONTAL, VERTICAL
from model.egresado_dao import obtener_datos_combinados, buscar, eliminar_egresado

def importar_excel():
    # Abre el cuadro de diálogo para seleccionar el archivo Excel
    archivo_excel = filedialog.askopenfilename(filetypes=[('Archivos Excel', '*.xlsx')])

    # Procesa el archivo Excel y realiza las operaciones necesarias
    # Aquí puedes agregar tu lógica para importar los datos del archivo Excel

    # Muestra un mensaje de éxito
    messagebox.showinfo('Importar Excel', 'Archivo Excel importado con éxito!')

def crear_ventana_importar_excel():
    ventana_importar_excel = tk.Toplevel()
    ventana_importar_excel.title('Importar Excel')

    # Agrega los componentes de la ventana importar excel
    etiqueta = tk.Label(ventana_importar_excel, text='Selecciona un archivo Excel:')
    etiqueta.pack()

    boton_importar = tk.Button(ventana_importar_excel, text='Importar', command=importar_excel)
    boton_importar.pack()


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu,  width=800, height=600)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Graficas')
    barra_menu.add_command(label='Ingresar Egresado')
    barra_menu.add_cascade(label='Importar Excel', command=crear_ventana_importar_excel)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=800, height=500)
        self.root = root
        self.pack()
        
        self.graficas_por_ventana = 4
        self.actual = 0
        self.fig = None
        self.axs = None
        self.btn_anterior = None
        self.btn_siguiente = None
        self.graficas = [self.generar_grafica_sexo,
                         self.generar_grafica_Carreradeegreso,
                         self.generar_grafica_maestria,
                         self.generar_grafica_situacionA,
                         self.generar_grafica_doctorado,
                         self.generar_grafica_calidadD,
                         self.generar_grafica_planestudio,
                         self.generar_grafica_oportunidadP,
                         self.generar_grafica_enfasisinvestigacion,
                         self.generar_grafica_satisfaccionestudio,
                         self.generar_grafica_experienciaresidencia,
                         self.generar_grafica_actividadactual,
                         self.generar_grafica_casotrabajar,
                         self.generar_grafica_medioempleo,
                         self.generar_grafica_requisitoscontratacion,
                         self.generar_grafica_antiguedadempleo,
                         self.generar_grafica_sectoreconomico,
                         self.generar_grafica_tamanoempresa,
                         self.generar_grafica_eficiencia,
                         self.generar_grafica_formacionacademica,
                         self.generar_grafica_utilidadresidencia,
                         self.generar_grafica_cursosactualizacion,
                         self.generar_grafica_posgrado
                         
                         ]

        

        self.tabla_egresados()

    def eliminar_registro(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning('Eliminar registro', 'No se ha seleccionado ningún registro.')
            return

        matricula = self.tabla.item(seleccion)['values'][1]  # Obtener la matrícula del registro seleccionado

        eliminado = eliminar_egresado(matricula)

        if eliminado:
            messagebox.showinfo('Eliminar registro', 'El registro se ha eliminado correctamente.')
            self.tabla.delete(seleccion)
        else:
            messagebox.showinfo('Eliminar registro', 'No se pudo eliminar el registro.')
    

 

    def generar_grafica_sexo(self, ax):
        # Obtener los datos de la columna "Sexo" de la tabla
        column_data = self.tabla.get_children()
        sexos = [self.tabla.item(item)['values'][5] for item in column_data]

        # Contar la cantidad de cada sexo
        cantidad_hombres = sexos.count('Hombre')
        cantidad_mujeres = sexos.count('Mujer')
        total_respuestas = len(sexos)

        # Configurar los datos de la gráfica de sexo
        labels_sexo = ['Hombre', 'Mujer']
        valores_sexo = [cantidad_hombres, cantidad_mujeres]
        colores_sexo = ['#0078D7', '#C70039']

        # Generar la gráfica de sexo en el subgráfico proporcionado
        wedges_sexo, texts_sexo, autotexts_sexo = ax.pie(valores_sexo, colors=colores_sexo, autopct='%1.1f%%', startangle=90)
        ax.set_title('Distribución de género')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de sexo
        for i, text in enumerate(autotexts_sexo):
            text.set_text(f"{valores_sexo[i]}")
            text.set_color(colores_sexo[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes = [f"{v / total_respuestas * 100:.1f}%" for v in valores_sexo]
        ax.legend(wedges_sexo, [f"{labels_sexo[i]}: {valores_sexo[i]} ({porcentajes[i]})" for i in range(len(labels_sexo))],
                  loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total: {total_respuestas}", transform=ax.transAxes, ha='center')


    def generar_grafica_Carreradeegreso(self, ax):
        # Obtener los datos de la columna "Nombre de la carrera" de la tabla
        column_data = self.tabla.get_children()
        carrera = [self.tabla.item(item)['values'][16] for item in column_data]

        # Contar la cantidad de cada carrera
        cantidad_sistemas = carrera.count('Ingeniería en Sistemas Computacionales')
        cantidad_ambiental = carrera.count('Ingeniería Ambiental')
        cantidad_bioquimica = carrera.count('Ingeniería Bioquímica')
        cantidad_civil = carrera.count('Ingeniería Civil')
        cantidad_electromecanica = carrera.count('Ingeniería Electromecánica')
        cantidad_industrial = carrera.count('Ingeniería Industrial')
        cantidad_administracion = carrera.count('Licenciatura en Administración')
        total_respuestas = len(carrera)

        # Configurar los datos de la gráfica de carrera de egreso
        labels_carrera = ['Ingeniería en Sistemas Computacionales', 'Ingeniería Ambiental', 'Ingeniería Bioquímica', 'Ingeniería Civil', 'Ingeniería Electromecánica', 'Ingeniería Industrial', 'Licenciatura en Administración']
        valores_carrera = [cantidad_sistemas, cantidad_ambiental, cantidad_bioquimica, cantidad_civil, cantidad_electromecanica, cantidad_industrial, cantidad_administracion]
        colores_carrera = ['#0078D7', '#C70039', '#FF5733', '#00B74A', '#FFC300', '#900C3F', '#009688']

        # Generar la gráfica de carrera de egreso en el subgráfico proporcionado
        wedges_carrera, texts_carrera, autotexts_carrera = ax.pie(valores_carrera, colors=colores_carrera, autopct='%1.1f%%', startangle=90)
        ax.set_title('Carrera de egreso')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de carrera de egreso
        for i, text in enumerate(autotexts_carrera):
            text.set_text(f"{valores_carrera[i]}")
            text.set_color(colores_carrera[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_carrera = [f"{v / total_respuestas * 100:.1f}%" for v in valores_carrera]
        ax.legend(wedges_carrera, [f"{labels_carrera[i]}: {valores_carrera[i]} ({porcentajes_carrera[i]})" for i in range(len(labels_carrera))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total: {total_respuestas}", transform=ax.transAxes, ha='center')


    def generar_grafica_maestria(self, ax):
        # Obtener los datos de la columna "Maestria" de la tabla
        column_data = self.tabla.get_children()
        maestria = [self.tabla.item(item)['values'][37] for item in column_data]

        # Contar la cantidad de cada maestria
        cantidad_Si = maestria.count('Sí')
        cantidad_No = maestria.count('No')
        total_respuestas = len(maestria)

        # Configurar los datos de la gráfica de maestria
        labels_maestria = ['Sí', 'No']
        valores_maestria = [cantidad_Si, cantidad_No]
        colores_maestria = ['#0078D7', '#C70039']

        # Generar la gráfica de maestria
        wedges_maestria, texts_maestria, autotexts_maestria = ax.pie(valores_maestria, colors=colores_maestria, autopct='%1.1f%%', startangle=90)
        ax.set_title('Tienes maestría')

        

        # Agregar anotaciones de cantidad en cada porción de la gráfica de maestría
        for i, text in enumerate(autotexts_maestria):
            text.set_text(f"{valores_maestria[i]}")
            text.set_color(colores_maestria[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_maestria = [f"{v / total_respuestas * 100:.1f}%" for v in valores_maestria]
        ax.legend(wedges_maestria, [f"{labels_maestria[i]}: {valores_maestria[i]} ({porcentajes_maestria[i]})" for i in range(len(labels_maestria))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas válidas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_situacionA(self, ax):
        # Obtener los datos de la columna "Situacion Academica" de la tabla
        column_data = self.tabla.get_children()
        situacionA = [self.tabla.item(item)['values'][42] for item in column_data]


            # Filtrar los datos vacíos
        situacionA = [dato for dato in situacionA if dato.strip()]

        if not situacionA:
            # Mostrar un mensaje en la consola
            print("No hay datos para generar la gráfica de Situacion Academica.")
            # Mostrar una gráfica de barras vacía
            ax.bar([], [])
            ax.set_title('No hay datos para generar la gráfica de Situacion Academica.')
        else:

            # Contar la cantidad de cada Situacion Academica 
            cantidad_Estudiante = situacionA.count('Estudiante')
            cantidad_Pasante = situacionA.count('Pasante')
            cantidad_Trunco = situacionA.count('Trunco')
            cantidad_Titulado = situacionA.count('Titulado')
            total_respuestas = len(situacionA)

            # Configurar los datos de la gráfica de maestria
            labels_situacionA = ['Estudiante', 'Pasante', 'Trunco', 'Titulado']
            valores_situacionA = [cantidad_Estudiante, cantidad_Pasante, cantidad_Trunco, cantidad_Titulado]
            colores_situacionA = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

            
            # Generar la gráfica de situacion academica
            wedges_maestria, texts_maestria, autotexts_maestria = ax.pie(valores_situacionA, colors=colores_situacionA, autopct='%1.1f%%', startangle=90)
            ax.set_title('Situacion Academica')

            
            # Agregar anotaciones de cantidad en cada porción de la gráfica de situación académica
            for i, text in enumerate(autotexts_maestria):
                text.set_text(f"{valores_situacionA[i]}")
                text.set_color(colores_situacionA[i])  # Asignar color a la anotación

            # Agregar leyenda fuera de la gráfica con los datos y colores
            porcentajes_situacionA = [f"{v / total_respuestas * 100:.1f}%" for v in valores_situacionA]
            ax.legend(wedges_maestria, [f"{labels_situacionA[i]}: {valores_situacionA[i]} ({porcentajes_situacionA[i]})" for i in range(len(labels_situacionA))],
                loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

            # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
            ax.text(0.5, -0.05, f"Total: {total_respuestas}", transform=ax.transAxes, ha='center')

        
    def generar_grafica_doctorado(self, ax):
        # Obtener los datos de la columna "Doctorado" de la tabla
        column_data = self.tabla.get_children()
        doctorado = [self.tabla.item(item)['values'][43] for item in column_data]

            # Filtrar los datos vacíos
        doctorado = [dato for dato in doctorado if dato.strip()]

        if not doctorado:
            # Mostrar un mensaje en la consola
            print("No hay datos para generar la gráfica de Doctorado.")
            # Mostrar una gráfica de barras vacía
            ax.bar([], [])
            ax.set_title('No hay datos para generar la gráfica de Doctorado.')
        else:
        
            # Contar la cantidad de cada doctorado
            cantidad_Si = doctorado.count('Si')
            cantidad_No = doctorado.count('No')
            total_respuestas = len(doctorado)

            # Configurar los datos de la gráfica de doctorado
            labels_doctorado = ['Si', 'No']
            valores_doctorado = [cantidad_Si, cantidad_No]
            colores_doctorado = ['#0078D7', '#C70039']

            
            # Generar la gráfica de doctorado
            wedges_doctorado, texts_doctorado, autotexts_doctorado = ax.pie(valores_doctorado, colors=colores_doctorado, autopct='%1.1f%%', startangle=90)
            ax.set_title('Tienes estudio de doctorado')

            # Agregar anotaciones de cantidad en cada porción de la gráfica de estudio de doctorado
            for i, text in enumerate(autotexts_doctorado):
                text.set_text(f"{valores_doctorado[i]}")
                text.set_color(colores_doctorado[i])  # Asignar color a la anotación

            # Agregar leyenda fuera de la gráfica con los datos y colores
            porcentajes_doctorado = [f"{v / total_respuestas * 100:.1f}%" for v in valores_doctorado]
            ax.legend(wedges_doctorado, [f"{labels_doctorado[i]}: {valores_doctorado[i]} ({porcentajes_doctorado[i]})" for i in range(len(labels_doctorado))],
                loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

            # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
            ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_calidadD(self, ax):
        # Obtener los datos de la columna "Calidad docentes" de la tabla
        column_data = self.tabla.get_children()
        calidadD = [self.tabla.item(item)['values'][48] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Muybuena = calidadD.count('Muy buena')
        cantidad_Buena = calidadD.count('Buena')
        cantidad_Regular = calidadD.count('Regular')
        cantidad_Mala = calidadD.count('Mala')
        total_respuestas = len(calidadD)

        # Configurar los datos de la gráfica de calidad docente
        labels_calidadD = ['Muy buena', 'Buena', 'Regular', 'Mala']
        valores_calidadD = [cantidad_Muybuena, cantidad_Buena, cantidad_Regular, cantidad_Mala]
        colores_calidadD = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        
        # Generar la gráfica de calidad docente
        wedges_calidadD, texts_calidadD, autotexts_calidadD = ax.pie(valores_calidadD, colors=colores_calidadD, autopct='%1.1f%%', startangle=90)
        ax.set_title('Calidad en los docentes')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de calidad docente
        for i, text in enumerate(autotexts_calidadD):
            text.set_text(f"{valores_calidadD[i]}")
            text.set_color(colores_calidadD[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_calidadD = [f"{v / total_respuestas * 100:.1f}%" for v in valores_calidadD]
        ax.legend(wedges_calidadD, [f"{labels_calidadD[i]}: {valores_calidadD[i]} ({porcentajes_calidadD[i]})" for i in range(len(labels_calidadD))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_planestudio(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        planestudio = [self.tabla.item(item)['values'][49] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Muybuena = planestudio.count('Muy buena')
        cantidad_Buena = planestudio.count('Buena')
        cantidad_Regular = planestudio.count('Regular')
        cantidad_Mala = planestudio.count('Mala')
        total_respuestas = len(planestudio)

        # Configurar los datos de la gráfica de Plan estudio
        labels_planestudio = ['Muy buena', 'Buena', 'Regular', 'Mala']
        valores_planestudio = [cantidad_Muybuena, cantidad_Buena, cantidad_Regular, cantidad_Mala]
        colores_planestudio = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        
        # Generar la gráfica de plan de estudio
        wedges_planestudio, texts_planestudio, autotexts_planestudio = ax.pie(valores_planestudio, colors=colores_planestudio, autopct='%1.1f%%', startangle=90)
        ax.set_title('Plan de estudio')


        # Agregar anotaciones de cantidad en cada porción de la gráfica de plan de estudio
        for i, text in enumerate(autotexts_planestudio):
            text.set_text(f"{valores_planestudio[i]}")
            text.set_color(colores_planestudio[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_planestudio = [f"{v / total_respuestas * 100:.1f}%" for v in valores_planestudio]
        ax.legend(wedges_planestudio, [f"{labels_planestudio[i]}: {valores_planestudio[i]} ({porcentajes_planestudio[i]})" for i in range(len(labels_planestudio))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_oportunidadP(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        oportunidadP = [self.tabla.item(item)['values'][50] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Muybuena = oportunidadP.count('Muy buena')
        cantidad_Buena = oportunidadP.count('Buena')
        cantidad_Regular = oportunidadP.count('Regular')
        cantidad_Mala = oportunidadP.count('Mala')
        total_respuestas = len(oportunidadP)

        # Configurar los datos de la gráfica de Plan estudio
        labels_oportunidadP = ['Muy buena', 'Buena', 'Regular', 'Mala']
        valores_oportunidadP = [cantidad_Muybuena, cantidad_Buena, cantidad_Regular, cantidad_Mala]
        colores_oportunidadP = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        
        # Generar la gráfica de Oportunidad de participar en proyectos de investigación y desarrollo
        wedges_oportunidadP, texts_oportunidadP, autotexts_oportunidadP = ax.pie(valores_oportunidadP, colors=colores_oportunidadP, autopct='%1.1f%%', startangle=90)
        ax.set_title('Oportunidad de participar en proyectos de investigación y desarrollo')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Oportunidad de participar en proyectos de investigación y desarrollo
        for i, text in enumerate(autotexts_oportunidadP):
            text.set_text(f"{valores_oportunidadP[i]}")
            text.set_color(colores_oportunidadP[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_oportunidadP = [f"{v / total_respuestas * 100:.1f}%" for v in valores_oportunidadP]
        ax.legend(wedges_oportunidadP, [f"{labels_oportunidadP[i]}: {valores_oportunidadP[i]} ({porcentajes_oportunidadP[i]})" for i in range(len(labels_oportunidadP))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_enfasisinvestigacion(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        oportunidadP = [self.tabla.item(item)['values'][51] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Muybuena = oportunidadP.count('Muy buena')
        cantidad_Buena = oportunidadP.count('Buena')
        cantidad_Regular = oportunidadP.count('Regular')
        cantidad_Mala = oportunidadP.count('Mala')
        total_respuestas = len(oportunidadP)

        # Configurar los datos de la gráfica de énfasis en la investigación dentro del proceso de enseñanza
        labels_enfasis = ['Muy buena', 'Buena', 'Regular', 'Mala']
        valores_enfasis = [cantidad_Muybuena, cantidad_Buena, cantidad_Regular, cantidad_Mala]
        colores_enfasis = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        
        # Generar la gráfica de énfasis en la investigación dentro del proceso de enseñanza
        wedges_enfasis, texts_enfasis, autotexts_enfasis = ax.pie(valores_enfasis, colors=colores_enfasis, autopct='%1.1f%%', startangle=90)
        ax.set_title('Énfasis que se le presta a la investigación dentro del proceso de enseñanza')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de énfasis en la investigación dentro del proceso de enseñanza
        for i, text in enumerate(autotexts_enfasis):
            text.set_text(f"{valores_enfasis[i]}")
            text.set_color(colores_enfasis[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_enfasis = [f"{v / total_respuestas * 100:.1f}%" for v in valores_enfasis]
        ax.legend(wedges_enfasis, [f"{labels_enfasis[i]}: {valores_enfasis[i]} ({porcentajes_enfasis[i]})" for i in range(len(labels_enfasis))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    

    def generar_grafica_satisfaccionestudio(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        oportunidadP = [self.tabla.item(item)['values'][52] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Muybuena = oportunidadP.count('Muy buena')
        cantidad_Buena = oportunidadP.count('Buena')
        cantidad_Regular = oportunidadP.count('Regular')
        cantidad_Mala = oportunidadP.count('Mala')
        total_respuestas = len(oportunidadP)

        # Configurar los datos de la gráfica de Satisfacción con las condiciones de estudio
        labels_satisfaccion = ['Muy buena', 'Buena', 'Regular', 'Mala']
        valores_satisfaccion = [cantidad_Muybuena, cantidad_Buena, cantidad_Regular, cantidad_Mala]
        colores_satisfaccion = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        # Generar la gráfica de Satisfacción con las condiciones de estudio
        wedges_satisfaccion, texts_satisfaccion, autotexts_satisfaccion = ax.pie(valores_satisfaccion, colors=colores_satisfaccion, autopct='%1.1f%%', startangle=90)
        ax.set_title('Satisfacción con las condiciones de estudio')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Satisfacción con las condiciones de estudio
        for i, text in enumerate(autotexts_satisfaccion):
            text.set_text(f"{valores_satisfaccion[i]}")
            text.set_color(colores_satisfaccion[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_satisfaccion = [f"{v / total_respuestas * 100:.1f}%" for v in valores_satisfaccion]
        ax.legend(wedges_satisfaccion, [f"{labels_satisfaccion[i]}: {valores_satisfaccion[i]} ({porcentajes_satisfaccion[i]})" for i in range(len(labels_satisfaccion))],
          loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_experienciaresidencia(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        oportunidadP = [self.tabla.item(item)['values'][53] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Muybuena = oportunidadP.count('Muy buena')
        cantidad_Buena = oportunidadP.count('Buena')
        cantidad_Regular = oportunidadP.count('Regular')
        cantidad_Mala = oportunidadP.count('Mala')
        total_respuestas = len(oportunidadP)

        # Configurar los datos de la gráfica de Experiencia obtenida a través de la residencia profesional
        labels_experiencia = ['Muy buena', 'Buena', 'Regular', 'Mala']
        valores_experiencia = [cantidad_Muybuena, cantidad_Buena, cantidad_Regular, cantidad_Mala]
        colores_experiencia = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        # Generar la gráfica de Experiencia obtenida a través de la residencia profesional
        wedges_experiencia, texts_experiencia, autotexts_experiencia = ax.pie(valores_experiencia, colors=colores_experiencia, autopct='%1.1f%%', startangle=90)
        ax.set_title('Experiencia obtenida a través de la residencia profesional')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Experiencia obtenida a través de la residencia profesional
        for i, text in enumerate(autotexts_experiencia):
            text.set_text(f"{valores_experiencia[i]}")
            text.set_color(colores_experiencia[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_experiencia = [f"{v / total_respuestas * 100:.1f}%" for v in valores_experiencia]
        ax.legend(wedges_experiencia, [f"{labels_experiencia[i]}: {valores_experiencia[i]} ({porcentajes_experiencia[i]})" for i in range(len(labels_experiencia))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_actividadactual(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        actividad_actual = [self.tabla.item(item)['values'][54] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Trabajo = actividad_actual.count('Trabajo')
        cantidad_Estudio = actividad_actual.count('Estudio')
        cantidad_EstudioTrabajo = actividad_actual.count('Estudio y Trabajo')
        cantidad_NoEstudioNiTrabajo = actividad_actual.count('No estudio, ni trabajo')
        total_respuestas = len(actividad_actual)

        # Configurar los datos de la gráfica de Actividad a la que se dedica actualmente
        labels_actividad = ['Trabajo', 'Estudio', 'Estudio y Trabajo', 'No estudio, ni trabajo']
        valores_actividad = [cantidad_Trabajo, cantidad_Estudio, cantidad_EstudioTrabajo, cantidad_NoEstudioNiTrabajo]
        colores_actividad = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        # Generar la gráfica de Actividad a la que se dedica actualmente
        wedges_actividad, texts_actividad, autotexts_actividad = ax.pie(valores_actividad, colors=colores_actividad, autopct='%1.1f%%', startangle=90)
        ax.set_title('Actividad a la que se dedica actualmente')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Actividad a la que se dedica actualmente
        for i, text in enumerate(autotexts_actividad):
            text.set_text(f"{valores_actividad[i]}\n({text.get_text()})")
            text.set_color(colores_actividad[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_actividad = [f"{v / total_respuestas * 100:.1f}%" for v in valores_actividad]
        ax.legend(wedges_actividad, [f"{labels_actividad[i]}: {valores_actividad[i]} ({porcentajes_actividad[i]})" for i in range(len(labels_actividad))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')


    def generar_grafica_casotrabajar(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        caso_trabajar = [self.tabla.item(item)['values'][55] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_AntesEgresar = caso_trabajar.count('Antes de egresar')
        cantidad_MenosSeisMeses = caso_trabajar.count('Menos de seis meses')
        cantidad_EntreSeisMesesUnAnio = caso_trabajar.count('Entre seis meses y un años')
        cantidad_MasUnAnio = caso_trabajar.count('Mas de un años')
        total_respuestas = len(caso_trabajar)

        # Configurar los datos de la gráfica de Tiempo transcurrido para obtener el primer empleo
        labels_caso_trabajar = ['Antes de egresar', 'Menos de seis meses', 'Entre seis meses y un años', 'Mas de un años']
        valores_caso_trabajar = [cantidad_AntesEgresar, cantidad_MenosSeisMeses, cantidad_EntreSeisMesesUnAnio, cantidad_MasUnAnio]
        colores_caso_trabajar = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        # Generar la gráfica de Tiempo transcurrido para obtener el primer empleo
        wedges_caso_trabajar, texts_caso_trabajar, autotexts_caso_trabajar = ax.pie(valores_caso_trabajar, colors=colores_caso_trabajar, autopct='%1.1f%%', startangle=90)
        ax.set_title('Tiempo transcurrido para obtener el primer empleo')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Tiempo transcurrido para obtener el primer empleo
        for i, text in enumerate(autotexts_caso_trabajar):
            text.set_text(f"{valores_caso_trabajar[i]}\n({text.get_text()})")
            text.set_color(colores_caso_trabajar[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_caso_trabajar = [f"{v / total_respuestas * 100:.1f}%" for v in valores_caso_trabajar]
        ax.legend(wedges_caso_trabajar, [f"{labels_caso_trabajar[i]}: {valores_caso_trabajar[i]} ({porcentajes_caso_trabajar[i]})" for i in range(len(labels_caso_trabajar))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_medioempleo(self, ax):
        # Obtener los datos de la columna "Medio para obtener empleo" de la tabla
        column_data = self.tabla.get_children()
        oportunidadP = [self.tabla.item(item)['values'][56] for item in column_data]

        # Contar la cantidad de cada Respuesta
        respuesta_counts = {}
        total_respuestas = len(oportunidadP)

        for respuesta in oportunidadP:
            if respuesta in respuesta_counts:
                respuesta_counts[respuesta] += 1
            else:
                respuesta_counts[respuesta] = 1

        # Configurar los datos de la gráfica de Medio para obtener empleo
        labels_medioempleo = list(respuesta_counts.keys())
        valores_medioempleo = list(respuesta_counts.values())

        # Obtener colores aleatorios para usar en la gráfica
        colores_medioempleo = list(mcolors.CSS4_COLORS.values())
        random.shuffle(colores_medioempleo)

        # Usar ciclo para repetir los colores en caso de que haya más respuestas que colores disponibles
        colores_medioempleo = cycle(colores_medioempleo)

        # Generar la gráfica de Medio para obtener empleo
        wedges_medioempleo, texts_medioempleo, autotexts_medioempleo = ax.pie(valores_medioempleo, colors=colores_medioempleo, autopct='%1.1f%%', startangle=90)
        ax.set_title('Medio para obtener empleo')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Medio para obtener empleo
        for i, text in enumerate(autotexts_medioempleo):
            text.set_text(f"{valores_medioempleo[i]}\n({text.get_text()})")
            text.set_color(next(colores_medioempleo))  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_medioempleo = [f"{v / total_respuestas * 100:.1f}%" for v in valores_medioempleo]
        ax.legend(wedges_medioempleo, [f"{labels_medioempleo[i]}: {valores_medioempleo[i]} ({porcentajes_medioempleo[i]})" for i in range(len(labels_medioempleo))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')



    def generar_grafica_requisitoscontratacion(self, ax):
        # Obtener los datos de la columna "Requisitos de contratacion" de la tabla
        column_data = self.tabla.get_children()
        oportunidadP = [self.tabla.item(item)['values'][57] for item in column_data]

        # Contar la cantidad de cada Respuesta
        respuesta_counts = {}
        total_respuestas = len(oportunidadP)

        for respuesta in oportunidadP:
            if respuesta in respuesta_counts:
                respuesta_counts[respuesta] += 1
            else:
                respuesta_counts[respuesta] = 1

        # Configurar los datos de la gráfica de Requisitos de contratacion
        labels_requisitos = list(respuesta_counts.keys())
        valores_requisitos = list(respuesta_counts.values())

        # Obtener colores aleatorios para usar en la gráfica
        colores_requisitos = list(mcolors.CSS4_COLORS.values())
        random.shuffle(colores_requisitos)

         # Usar ciclo para repetir los colores en caso de que haya más respuestas que colores disponibles
        colores_requisitos = cycle(colores_requisitos)

        # Generar la gráfica de Requisitos de contratacion
        wedges_requisitos, texts_requisitos, autotexts_requisitos = ax.pie(valores_requisitos, colors=colores_requisitos, autopct='%1.1f%%', startangle=90)
        ax.set_title('Requisitos de contratacion')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Requisitos de contratacion
        for i, text in enumerate(autotexts_requisitos):
            text.set_text(f"{valores_requisitos[i]}\n({text.get_text()})")
            text.set_color(next(colores_requisitos))  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_requisitos = [f"{v / total_respuestas * 100:.1f}%" for v in valores_requisitos]
        ax.legend(wedges_requisitos, [f"{labels_requisitos[i]}: {valores_requisitos[i]} ({porcentajes_requisitos[i]})" for i in range(len(labels_requisitos))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')


    def generar_grafica_antiguedadempleo(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        antiguedad_empleo = [self.tabla.item(item)['values'][58] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_MenosUnAnio = antiguedad_empleo.count('Menos de un año')
        cantidad_UnAnio = antiguedad_empleo.count('Un año')
        cantidad_DosAnios = antiguedad_empleo.count('Dos años')
        cantidad_TresAnios = antiguedad_empleo.count('Tres años')
        cantidad_MasTresAnios = antiguedad_empleo.count('Mas de tres años')
        total_respuestas = len(antiguedad_empleo)

        # Configurar los datos de la gráfica de Antigüedad en el empleo
        labels_antiguedad = ['Menos de un año', 'Un año', 'Dos años', 'Tres años', 'Mas de tres años']
        valores_antiguedad = [cantidad_MenosUnAnio, cantidad_UnAnio, cantidad_DosAnios, cantidad_TresAnios, cantidad_MasTresAnios]
        colores_antiguedad = ['#0078D7', '#C70039', '#FF5733', '#00B74A', '#FFA500']

        # Generar la gráfica de Antigüedad en el empleo
        wedges_antiguedad, texts_antiguedad, autotexts_antiguedad = ax.pie(valores_antiguedad, colors=colores_antiguedad, autopct='%1.1f%%', startangle=90)
        ax.set_title('Antigüedad en el empleo')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Antigüedad en el empleo
        for i, text in enumerate(autotexts_antiguedad):
            text.set_text(f"{valores_antiguedad[i]}\n({text.get_text()})")
            text.set_color(colores_antiguedad[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_antiguedad = [f"{v / total_respuestas * 100:.1f}%" for v in valores_antiguedad]
        ax.legend(wedges_antiguedad, [f"{labels_antiguedad[i]}: {valores_antiguedad[i]} ({porcentajes_antiguedad[i]})" for i in range(len(labels_antiguedad))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    
    def generar_grafica_sectoreconomico(self, ax):
        # Obtener los datos de la columna "Sector economico" de la tabla
        column_data = self.tabla.get_children()
        oportunidadP = [self.tabla.item(item)['values'][85] for item in column_data]

        # Contar la cantidad de cada Respuesta
        respuesta_counts = {}
        total_respuestas = len(oportunidadP)

        for respuesta in oportunidadP:
            if respuesta in respuesta_counts:
                respuesta_counts[respuesta] += 1
            else:
                respuesta_counts[respuesta] = 1

        # Configurar los datos de la gráfica de Sector economico
        labels_sectoreconomico = list(respuesta_counts.keys())
        valores_sectoreconomico = list(respuesta_counts.values())

        # Obtener colores aleatorios para usar en la gráfica
        colores_sectoreconomico = list(mcolors.CSS4_COLORS.values())
        random.shuffle(colores_sectoreconomico)

        # Usar ciclo para repetir los colores en caso de que haya más respuestas que colores disponibles
        colores_sectoreconomico = cycle(colores_sectoreconomico)

        # Generar la gráfica de Sector economico
        wedges_sectoreconomico, texts_sectoreconomico, autotexts_sectoreconomico = ax.pie(valores_sectoreconomico, colors=colores_sectoreconomico, autopct='%1.1f%%', startangle=90)
        ax.set_title('Sector economico de la empresa u organizacion')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Sector economico
        for i, text in enumerate(autotexts_sectoreconomico):
            text.set_text(f"{valores_sectoreconomico[i]}\n({text.get_text()})")
            text.set_color(next(colores_sectoreconomico))  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_sectoreconomico = [f"{v / total_respuestas * 100:.1f}%" for v in valores_sectoreconomico]
        ax.legend(wedges_sectoreconomico, [f"{labels_sectoreconomico[i]}: {valores_sectoreconomico[i]} ({porcentajes_sectoreconomico[i]})" for i in range(len(labels_sectoreconomico))],
                loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')


# Uso de la función:

    def generar_grafica_tamanoempresa(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        tamano_empresa = [self.tabla.item(item)['values'][86] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Microempresa = tamano_empresa.count('Microempresa (1 a 30 personas)')
        cantidad_Pequeña = tamano_empresa.count('Pequeña (31 a 100 personas)')
        cantidad_Mediana = tamano_empresa.count('Mediana (101 a 500 personas)')
        cantidad_Grande = tamano_empresa.count('Grande (Más de 500)')
        total_respuestas = len(tamano_empresa)

        # Configurar los datos de la gráfica de Tamaño de la empresa u organización
        labels_tamano = ['Microempresa (1 a 30 personas)', 'Pequeña (31 a 100 personas)', 'Mediana (101 a 500 personas)', 'Grande (Más de 500)']
        valores_tamano = [cantidad_Microempresa, cantidad_Pequeña, cantidad_Mediana, cantidad_Grande]
        colores_tamano = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        # Generar la gráfica de Tamaño de la empresa u organización
        wedges_tamano, texts_tamano, autotexts_tamano = ax.pie(valores_tamano, colors=colores_tamano, autopct='%1.1f%%', startangle=90)
        ax.set_title('Tamaño de la empresa u organización')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Tamaño de la empresa u organización
        for i, text in enumerate(autotexts_tamano):
            text.set_text(f"{valores_tamano[i]}\n({text.get_text()})")
            text.set_color(colores_tamano[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_tamano = [f"{v / total_respuestas * 100:.1f}%" for v in valores_tamano]
        ax.legend(wedges_tamano, [f"{labels_tamano[i]}: {valores_tamano[i]} ({porcentajes_tamano[i]})" for i in range(len(labels_tamano))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')



    def generar_grafica_eficiencia(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        eficiencia = [self.tabla.item(item)['values'][87] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_MuyEficiente = eficiencia.count('Muy eficiente')
        cantidad_Eficiente = eficiencia.count('Eficiente')
        cantidad_PocoEficiente = eficiencia.count('Poco eficiente')
        cantidad_Deficiente = eficiencia.count('Deficiente')
        total_respuestas = len(eficiencia)

        # Configurar los datos de la gráfica de Eficiencia para realizar las actividades laborales
        labels_eficiencia = ['Muy eficiente', 'Eficiente', 'Poco eficiente', 'Deficiente']
        valores_eficiencia = [cantidad_MuyEficiente, cantidad_Eficiente, cantidad_PocoEficiente, cantidad_Deficiente]
        colores_eficiencia = ['#0078D7', '#C70039', '#FF5733', '#00B74A']

        # Generar la gráfica de Eficiencia para realizar las actividades laborales
        wedges_eficiencia, texts_eficiencia, autotexts_eficiencia = ax.pie(valores_eficiencia, colors=colores_eficiencia, autopct='%1.1f%%', startangle=90)
        ax.set_title('Eficiencia para realizar las actividades laborales')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Eficiencia para realizar las actividades laborales
        for i, text in enumerate(autotexts_eficiencia):
            text.set_text(f"{valores_eficiencia[i]}\n({text.get_text()})")
            text.set_color(colores_eficiencia[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_eficiencia = [f"{v / total_respuestas * 100:.1f}%" for v in valores_eficiencia]
        ax.legend(wedges_eficiencia, [f"{labels_eficiencia[i]}: {valores_eficiencia[i]} ({porcentajes_eficiencia[i]})" for i in range(len(labels_eficiencia))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_formacionacademica(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        formacion_academica = [self.tabla.item(item)['values'][88] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Excelente = formacion_academica.count('Excelente')
        cantidad_Bueno = formacion_academica.count('Bueno')
        cantidad_Regular = formacion_academica.count('Regular')
        cantidad_Malo = formacion_academica.count('Malo')
        cantidad_Pesimo = formacion_academica.count('Pesimo')
        total_respuestas = len(formacion_academica)

        # Configurar los datos de la gráfica de Formación Académica con respecto a desempeño laboral
        labels_formacion_academica = ['Excelente', 'Bueno', 'Regular', 'Malo', 'Pesimo']
        valores_formacion_academica = [cantidad_Excelente, cantidad_Bueno, cantidad_Regular, cantidad_Malo, cantidad_Pesimo]
        colores_formacion_academica = ['#0078D7', '#C70039', '#FF5733', '#00B74A', '#FFC300']

        # Generar la gráfica de Formación Académica con respecto a desempeño laboral
        wedges_formacion_academica, texts_formacion_academica, autotexts_formacion_academica = ax.pie(valores_formacion_academica, colors=colores_formacion_academica, autopct='%1.1f%%', startangle=90)
        ax.set_title('Cómo califica su formación académica con respecto a su desempeño laboral')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Formación Académica con respecto a desempeño laboral
        for i, text in enumerate(autotexts_formacion_academica):
            text.set_text(f"{valores_formacion_academica[i]}\n({text.get_text()})")
            text.set_color(colores_formacion_academica[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_formacion_academica = [f"{v / total_respuestas * 100:.1f}%" for v in valores_formacion_academica]
        ax.legend(wedges_formacion_academica, [f"{labels_formacion_academica[i]}: {valores_formacion_academica[i]} ({porcentajes_formacion_academica[i]})" for i in range(len(labels_formacion_academica))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_utilidadresidencia(self, ax):
        # Obtener los datos de la columna "Plan de estudio" de la tabla
        column_data = self.tabla.get_children()
        utilidad_residencia = [self.tabla.item(item)['values'][89] for item in column_data]

        # Contar la cantidad de cada Respuesta
        cantidad_Excelente = utilidad_residencia.count('Excelente')
        cantidad_Bueno = utilidad_residencia.count('Bueno')
        cantidad_Regular = utilidad_residencia.count('Regular')
        cantidad_Malo = utilidad_residencia.count('Malo')
        cantidad_Pesimo = utilidad_residencia.count('Pesimo')
        total_respuestas = len(utilidad_residencia)

        # Configurar los datos de la gráfica de Utilidad de las residencias profesionales o prácticas profesionales para el desarrollo laboral y profesional
        labels_utilidad_residencia = ['Excelente', 'Bueno', 'Regular', 'Malo', 'Pesimo']
        valores_utilidad_residencia = [cantidad_Excelente, cantidad_Bueno, cantidad_Regular, cantidad_Malo, cantidad_Pesimo]
        colores_utilidad_residencia = ['#0078D7', '#C70039', '#FF5733', '#00B74A', '#FFC300']

        # Generar la gráfica de Utilidad de las residencias profesionales o prácticas profesionales para el desarrollo laboral y profesional
        wedges_utilidad_residencia, texts_utilidad_residencia, autotexts_utilidad_residencia = ax.pie(valores_utilidad_residencia, colors=colores_utilidad_residencia, autopct='%1.1f%%', startangle=90)
        ax.set_title('Utilidad de las residencias profesionales o prácticas profesionales para el desarrollo laboral y profesional')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Utilidad de las residencias profesionales o prácticas profesionales
        for i, text in enumerate(autotexts_utilidad_residencia):
            text.set_text(f"{valores_utilidad_residencia[i]}\n({text.get_text()})")
            text.set_color(colores_utilidad_residencia[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_utilidad_residencia = [f"{v / total_respuestas * 100:.1f}%" for v in valores_utilidad_residencia]
        ax.legend(wedges_utilidad_residencia, [f"{labels_utilidad_residencia[i]}: {valores_utilidad_residencia[i]} ({porcentajes_utilidad_residencia[i]})" for i in range(len(labels_utilidad_residencia))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_cursosactualizacion(self, ax):
        # Obtener los datos de la columna "Cursos de actualización" de la tabla
        column_data = self.tabla.get_children()
        cursos_actualizacion = [self.tabla.item(item)['values'][100] for item in column_data]

        # Contar la cantidad de cada respuesta
        cantidad_Si = cursos_actualizacion.count('Sí')
        cantidad_No = cursos_actualizacion.count('No')
        total_respuestas = len(cursos_actualizacion)

        # Configurar los datos de la gráfica de Cursos de actualización
        labels_cursos_actualizacion = ['Sí', 'No']
        valores_cursos_actualizacion = [cantidad_Si, cantidad_No]
        colores_cursos_actualizacion = ['#0078D7', '#C70039']

        # Generar la gráfica de Cursos de actualización
        wedges_cursos_actualizacion, texts_cursos_actualizacion, autotexts_cursos_actualizacion = ax.pie(valores_cursos_actualizacion, colors=colores_cursos_actualizacion, autopct='%1.1f%%', startangle=90)
        ax.set_title('Le gustaría tomar cursos de actualización')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Cursos de actualización
        for i, text in enumerate(autotexts_cursos_actualizacion):
            text.set_text(f"{valores_cursos_actualizacion[i]}\n({text.get_text()})")
            text.set_color(colores_cursos_actualizacion[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_cursos_actualizacion = [f"{v / total_respuestas * 100:.1f}%" for v in valores_cursos_actualizacion]
        ax.legend(wedges_cursos_actualizacion, [f"{labels_cursos_actualizacion[i]}: {valores_cursos_actualizacion[i]} ({porcentajes_cursos_actualizacion[i]})" for i in range(len(labels_cursos_actualizacion))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')

    def generar_grafica_posgrado(self, ax):
        # Obtener los datos de la columna "Posgrado" de la tabla
        column_data = self.tabla.get_children()
        posgrado = [self.tabla.item(item)['values'][102] for item in column_data]

        # Contar la cantidad de cada respuesta
        cantidad_Si = posgrado.count('Sí')
        cantidad_No = posgrado.count('No')
        total_respuestas = len(posgrado)

        # Configurar los datos de la gráfica de Posgrado
        labels_posgrado = ['Sí', 'No']
        valores_posgrado = [cantidad_Si, cantidad_No]
        colores_posgrado = ['#0078D7', '#C70039']

        # Generar la gráfica de Posgrado
        wedges_posgrado, texts_posgrado, autotexts_posgrado = ax.pie(valores_posgrado, colors=colores_posgrado, autopct='%1.1f%%', startangle=90)
        ax.set_title('Le gustaría tomar algún Posgrado')

        # Agregar anotaciones de cantidad en cada porción de la gráfica de Posgrado
        for i, text in enumerate(autotexts_posgrado):
            text.set_text(f"{valores_posgrado[i]}\n({text.get_text()})")
            text.set_color(colores_posgrado[i])  # Asignar color a la anotación

        # Agregar leyenda fuera de la gráfica con los datos y colores
        porcentajes_posgrado = [f"{v / total_respuestas * 100:.1f}%" for v in valores_posgrado]
        ax.legend(wedges_posgrado, [f"{labels_posgrado[i]}: {valores_posgrado[i]} ({porcentajes_posgrado[i]})" for i in range(len(labels_posgrado))],
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Agregar anotación adicional con el número total de respuestas (movido hacia arriba)
        ax.text(0.5, -0.05, f"Total respuestas: {total_respuestas}", transform=ax.transAxes, ha='center')


    def generar_graficas(self):
        # Cerrar todas las figuras abiertas previas
        plt.close('all')

        # Crear la figura y el subgráfico
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        plt.subplots_adjust(bottom=0.15)  # Ajustar la posición de los botones

        # Limpiar el subgráfico
        self.ax.clear()

        # Generar la gráfica en el subgráfico
        self.graficas[self.actual](self.ax)

        # Mostrar los botones de navegación
        self.mostrar_botones_navegacion()

        # Agregar un pequeño retardo antes de mostrar la ventana actual
        self.update_idletasks()
        time.sleep(0.1)

        # Mostrar la ventana actual
        plt.show()

    def mostrar_botones_navegacion(self):
        # Posición y tamaño de los botones
        pos_x = 0.4
        pos_y = 0.05
        width = 0.1
        height = 0.04
        spacing = 0.03

        # Crear el botón "Anterior" si es posible retroceder
        if self.btn_anterior is not None:
            self.btn_anterior.disconnect_events()  # Desconectar eventos anteriores
            self.btn_anterior.ax.remove()  # Eliminar el botón anterior
        if self.actual > 0:
            btn_anterior_ax = self.fig.add_axes([pos_x, pos_y, width, height])
            self.btn_anterior = Button(btn_anterior_ax, 'Anterior')
            self.btn_anterior.on_clicked(self.anterior)

        # Crear el botón "Siguiente" si es posible avanzar
        pos_x += width + spacing
        if self.btn_siguiente is not None:
            self.btn_siguiente.disconnect_events()  # Desconectar eventos anteriores
            self.btn_siguiente.ax.remove()  # Eliminar el botón anterior
        if self.actual < len(self.graficas) - 1:
            btn_siguiente_ax = self.fig.add_axes([pos_x, pos_y, width, height])
            self.btn_siguiente = Button(btn_siguiente_ax, 'Siguiente')
            self.btn_siguiente.on_clicked(self.siguiente)

        # Actualizar la figura para mostrar los botones
        self.fig.canvas.draw()

    def anterior(self, event):
        self.actual -= 1
        if self.actual < 0:
            self.actual = 0
        self.cerrar_figura()
        self.generar_graficas()

    def siguiente(self, event):
        self.actual += 1
        if self.actual >= len(self.graficas):
            self.actual = len(self.graficas) - 1
        self.cerrar_figura()
        self.generar_graficas()

    def cerrar_figura(self):
        if self.fig is not None:
            # Desconectar eventos de los botones antes de cerrar la figura
            if self.btn_anterior is not None:
                self.btn_anterior.disconnect_events()
            if self.btn_siguiente is not None:
                self.btn_siguiente.disconnect_events()

            # Cerrar la ventana que contiene la figura
            manager = self.fig.canvas.manager
            if manager is not None:
                manager.destroy()

            # Eliminar referencias a la figura y el toolbar
            self.fig = None
            self.ax = None

    def tabla_egresados(self):
        # Recuperar la lista de egresados
        datos_combinados = obtener_datos_combinados()
        datos_combinados.reverse()

        
       

        self.tabla = ttk.Treeview(self, height=20)
        self.tabla.grid(row=4, column=0, columnspan=4)

        self.entry_busqueda = tk.Entry(self)
        self.entry_busqueda.config(width=30, font=('Arial', 12))
        self.entry_busqueda.grid(row=0, column=0, padx=10, pady=10)

        
        self.boton_buscar = tk.Button(self, text="Buscar", command=self.realizar_busqueda)
        self.boton_buscar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#0078D7',
                                 cursor='hand2', activebackground='#005299')
        self.boton_buscar.grid(row=0, column=1, padx=10, pady=10)

      

        ladoy = Scrollbar(self, orient=VERTICAL, command=self.tabla.yview)
        ladoy.grid(row=4, column=4, rowspan=2, sticky='ns')

        ladox = Scrollbar(self, orient=HORIZONTAL, command=self.tabla.xview)
        ladox.grid(column=0, row=5, columnspan=4, sticky='ew')

        self.tabla.configure(yscrollcommand=ladoy.set, xscrollcommand=ladox.set)
        self.tabla['columns'] = ('Matricula', 'DireccionCorreoElectronico', 'Nombre', 'ApellidoPaterno', 'ApellidoMaterno', 'Sexo',
               'EstadoCivil', 'TelefonoCelular', 'TelefonoCasa', 'Calle', 'Numero', 'Colonia', 'CodigoPostal',
               'Ciudad', 'Municipio', 'Estado', 'NombreCarrera', 'EspecialidadDeEgreso', 'AñoDeEgreso', 'MesDeEgreso', 'DominioIdiomaIngles',
               'DominioIdiomaFrances', 'DominioIdiomaItaliano', 'DominioIdiomaAleman', 'DominioIdiomaJapones', 'DominioPaqueteWord', 'DominioPaqueteExcel',
               'DominioPaquetePowerPoint','DominioPaqueteAccess','DominioPaqueteWindows', 'DominioPaqueteLinux', 'DominioPaqueteSolidworks', 'DominioPaqueteAutocad',
               'DominioPaqueteAspelNOI', 'DominioPaqueteAspelCOI', 'DominioPaqueteAspelBancos', 'Certificaciones', 'TieneMaestria', 'NombreMaestria',
               'InstitucionMaestria', 'PaisMaestria', 'AnoIngreso', 'SituacionAcademica', 'TieneDoctorado', 'NombreDoctorado', 'InstitucionDoctorado',
               'AnoIngreso2', 'SituacionAcademica2', 'CalidadD', 'PlanE', 'OportunidadP', 'EnfasisI', 'SatisfaccionE', 'ExperienciaR', '53', '54', '55','56',
               '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
               '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103',
               '104', '105', '106', '107', '108', '109'
               )

        # Configurar las columnas de la tabla
        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Matricula', minwidth=100, width=120, anchor='center')
        self.tabla.column('DireccionCorreoElectronico', minwidth=100, width=160, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=120, anchor='center')
        self.tabla.column('ApellidoPaterno', minwidth=100, width=120, anchor='center')
        self.tabla.column('ApellidoMaterno', minwidth=100, width=120, anchor='center')
        self.tabla.column('Sexo', minwidth=100, width=120, anchor='center')
        self.tabla.column('EstadoCivil', minwidth=100, width=120, anchor='center')
        self.tabla.column('TelefonoCelular', minwidth=100, width=120, anchor='center')
        self.tabla.column('TelefonoCasa', minwidth=100, width=120, anchor='center')
        self.tabla.column('Calle', minwidth=100, width=120, anchor='center')
        self.tabla.column('Numero', minwidth=100, width=120, anchor='center')
        self.tabla.column('Colonia', minwidth=100, width=120, anchor='center')
        self.tabla.column('CodigoPostal', minwidth=100, width=120, anchor='center')
        self.tabla.column('Ciudad', minwidth=100, width=120, anchor='center')
        self.tabla.column('Municipio', minwidth=100, width=120, anchor='center')
        self.tabla.column('Estado', minwidth=100, width=120, anchor='center')
        self.tabla.column('NombreCarrera', minwidth=100, width=120, anchor='center')
        self.tabla.column('EspecialidadDeEgreso', minwidth=100, width=120, anchor='center')
        self.tabla.column('AñoDeEgreso', minwidth=100, width=120, anchor='center')
        self.tabla.column('MesDeEgreso', minwidth=100, width=120, anchor='center')
        self.tabla.column('DominioIdiomaIngles', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioIdiomaFrances', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioIdiomaItaliano', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioIdiomaAleman', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioIdiomaJapones', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteWord', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteExcel', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaquetePowerPoint', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteAccess', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteWindows', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteLinux', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteSolidworks', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteAutocad', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteAspelNOI', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteAspelCOI', minwidth=100, width=160, anchor='center')
        self.tabla.column('DominioPaqueteAspelBancos', minwidth=100, width=160, anchor='center')
        self.tabla.column('Certificaciones', minwidth=100, width=160, anchor='center')
        self.tabla.column('TieneMaestria', minwidth=100, width=160, anchor='center')
        self.tabla.column('NombreMaestria', minwidth=100, width=160, anchor='center')
        self.tabla.column('InstitucionMaestria', minwidth=100, width=160, anchor='center')
        self.tabla.column('PaisMaestria', minwidth=100, width=160, anchor='center')
        self.tabla.column('AnoIngreso', minwidth=100, width=160, anchor='center')
        self.tabla.column('SituacionAcademica', minwidth=100, width=160, anchor='center')
        self.tabla.column('TieneDoctorado', minwidth=100, width=160, anchor='center')
        self.tabla.column('NombreDoctorado', minwidth=100, width=160, anchor='center')
        self.tabla.column('InstitucionDoctorado', minwidth=100, width=160, anchor='center')
        self.tabla.column('AnoIngreso2', minwidth=100, width=160, anchor='center')
        self.tabla.column('SituacionAcademica2', minwidth=100, width=160, anchor='center')
        self.tabla.column('CalidadD', minwidth=100, width=160, anchor='center')
        self.tabla.column('PlanE', minwidth=100, width=160, anchor='center')
        self.tabla.column('OportunidadP', minwidth=100, width=160, anchor='center')
        self.tabla.column('EnfasisI', minwidth=100, width=160, anchor='center')
        self.tabla.column('SatisfaccionE', minwidth=100, width=160, anchor='center')
        self.tabla.column('ExperienciaR', minwidth=100, width=160, anchor='center')
        self.tabla.column('53', minwidth=100, width=160, anchor='center')
        self.tabla.column('54', minwidth=100, width=160, anchor='center')
        self.tabla.column('55', minwidth=100, width=160, anchor='center')
        self.tabla.column('56', minwidth=100, width=160, anchor='center')
        self.tabla.column('57', minwidth=100, width=160, anchor='center')
        self.tabla.column('58', minwidth=100, width=160, anchor='center')
        self.tabla.column('59', minwidth=100, width=160, anchor='center')
        self.tabla.column('60', minwidth=100, width=160, anchor='center')
        self.tabla.column('61', minwidth=100, width=160, anchor='center')
        self.tabla.column('62', minwidth=100, width=160, anchor='center')
        self.tabla.column('63', minwidth=100, width=160, anchor='center')
        self.tabla.column('64', minwidth=100, width=160, anchor='center')
        self.tabla.column('65', minwidth=100, width=160, anchor='center')
        self.tabla.column('66', minwidth=100, width=160, anchor='center')
        self.tabla.column('67', minwidth=100, width=160, anchor='center')
        self.tabla.column('68', minwidth=100, width=160, anchor='center')
        self.tabla.column('69', minwidth=100, width=160, anchor='center')
        self.tabla.column('70', minwidth=100, width=160, anchor='center')
        self.tabla.column('71', minwidth=100, width=160, anchor='center')
        self.tabla.column('72', minwidth=100, width=160, anchor='center')
        self.tabla.column('73', minwidth=100, width=160, anchor='center')
        self.tabla.column('74', minwidth=100, width=160, anchor='center')
        self.tabla.column('75', minwidth=100, width=160, anchor='center')
        self.tabla.column('76', minwidth=100, width=160, anchor='center')
        self.tabla.column('77', minwidth=100, width=160, anchor='center')
        self.tabla.column('78', minwidth=100, width=160, anchor='center')
        self.tabla.column('79', minwidth=100, width=160, anchor='center')
        self.tabla.column('80', minwidth=100, width=160, anchor='center')
        self.tabla.column('81', minwidth=100, width=160, anchor='center')
        self.tabla.column('82', minwidth=100, width=160, anchor='center')
        self.tabla.column('83', minwidth=100, width=160, anchor='center')
        self.tabla.column('84', minwidth=100, width=160, anchor='center')
        self.tabla.column('85', minwidth=100, width=160, anchor='center')
        self.tabla.column('86', minwidth=100, width=160, anchor='center')
        self.tabla.column('87', minwidth=100, width=160, anchor='center')
        self.tabla.column('88', minwidth=100, width=160, anchor='center')
        self.tabla.column('89', minwidth=100, width=160, anchor='center')
        self.tabla.column('90', minwidth=100, width=160, anchor='center')
        self.tabla.column('91', minwidth=100, width=160, anchor='center')
        self.tabla.column('92', minwidth=100, width=160, anchor='center')
        self.tabla.column('93', minwidth=100, width=160, anchor='center')
        self.tabla.column('94', minwidth=100, width=160, anchor='center')
        self.tabla.column('95', minwidth=100, width=160, anchor='center')
        self.tabla.column('96', minwidth=100, width=160, anchor='center')
        self.tabla.column('97', minwidth=100, width=160, anchor='center')
        self.tabla.column('98', minwidth=100, width=160, anchor='center')
        self.tabla.column('99', minwidth=100, width=160, anchor='center')
        self.tabla.column('100', minwidth=100, width=160, anchor='center')
        self.tabla.column('101', minwidth=100, width=160, anchor='center')
        self.tabla.column('102', minwidth=100, width=160, anchor='center')
        self.tabla.column('103', minwidth=100, width=160, anchor='center')
        self.tabla.column('104', minwidth=100, width=160, anchor='center')
        self.tabla.column('105', minwidth=100, width=160, anchor='center')
        self.tabla.column('106', minwidth=100, width=160, anchor='center')
        self.tabla.column('107', minwidth=100, width=160, anchor='center')
        self.tabla.column('108', minwidth=100, width=160, anchor='center')
        self.tabla.column('109', minwidth=100, width=160, anchor='center')
        
       

        # Configurar las cabeceras de las columnas
        self.tabla.heading('#0', text='Número')
        self.tabla.heading('Matricula', text='Matrícula')
        self.tabla.heading('DireccionCorreoElectronico', text='Correo Electronico')
        self.tabla.heading('Nombre', text='Nombre')
        self.tabla.heading('ApellidoPaterno', text='Apellido Paterno')
        self.tabla.heading('ApellidoMaterno', text='Apellido Materno')
        self.tabla.heading('Sexo', text='Sexo')
        self.tabla.heading('EstadoCivil', text='Estado Civil')
        self.tabla.heading('TelefonoCelular', text='Telefono Celular')
        self.tabla.heading('TelefonoCasa', text='Telefono de casa')
        self.tabla.heading('Calle', text='Calle')
        self.tabla.heading('Numero', text='Numero de calle')
        self.tabla.heading('Colonia', text='Colonia')
        self.tabla.heading('CodigoPostal', text='Codigo Postal')
        self.tabla.heading('Ciudad', text='Ciudad')
        self.tabla.heading('Municipio', text='Municipio')
        self.tabla.heading('Estado', text='Estado')
        self.tabla.heading('NombreCarrera', text='Nombre de la carrera')
        self.tabla.heading('EspecialidadDeEgreso', text='Especialidad de egreso')
        self.tabla.heading('AñoDeEgreso', text='Año de egreso')
        self.tabla.heading('MesDeEgreso', text='Mes de egreso')
        self.tabla.heading('DominioIdiomaIngles', text='Dominio del idioma Ingles')
        self.tabla.heading('DominioIdiomaFrances', text='Dominio del idioma Frances')
        self.tabla.heading('DominioIdiomaItaliano', text='Dominio del idioma Italiano')
        self.tabla.heading('DominioIdiomaAleman', text='Dominio del idioma Aleman')
        self.tabla.heading('DominioIdiomaJapones', text='Dominio del idioma Japones')
        self.tabla.heading('DominioPaqueteWord', text='Dominio del paquete Word')
        self.tabla.heading('DominioPaqueteExcel', text='Dominio del paquete Excel')
        self.tabla.heading('DominioPaquetePowerPoint', text='Dominio del paquete PowerPoint')
        self.tabla.heading('DominioPaqueteAccess', text='Dominio del paquete Access')
        self.tabla.heading('DominioPaqueteWindows', text='Dominio del paquete Windows')
        self.tabla.heading('DominioPaqueteLinux', text='Dominio del paquete Linux')
        self.tabla.heading('DominioPaqueteSolidworks', text='Dominio del paquete Solidworks')
        self.tabla.heading('DominioPaqueteAutocad', text='Dominio del paquete Autocad')
        self.tabla.heading('DominioPaqueteAspelNOI', text='Dominio del paquete ASPELNOI')
        self.tabla.heading('DominioPaqueteAspelCOI', text='Dominio del paquete ASPELCOI')
        self.tabla.heading('DominioPaqueteAspelBancos', text='Dominio del paquete ASPELBancos')
        self.tabla.heading('Certificaciones', text='En caso que tenga certificaciones, por favor escriba las que tiene.')
        self.tabla.heading('TieneMaestria', text='¿Tienes Maestría? o ¿Estudias Maestría?')
        self.tabla.heading('NombreMaestria', text='Nombre de la Maestría')
        self.tabla.heading('InstitucionMaestria', text='Institución donde estudio la Maestría')
        self.tabla.heading('PaisMaestria', text='País donde estudio la Maestría')
        self.tabla.heading('AnoIngreso', text='Año de ingreso')
        self.tabla.heading('SituacionAcademica', text='Situación académica')
        self.tabla.heading('TieneDoctorado', text='¿Tiene doctorado?')
        self.tabla.heading('NombreDoctorado', text='Nombre del doctorado')
        self.tabla.heading('InstitucionDoctorado', text='Institucion del doctorado')
        self.tabla.heading('AnoIngreso2', text='Año de ingreso')
        self.tabla.heading('SituacionAcademica2', text='Situación académica')
        self.tabla.heading('CalidadD', text='II.1 Calidad de los docentes')
        self.tabla.heading('PlanE', text='II.2 Plan de Estudios')
        self.tabla.heading('OportunidadP', text='II.3  Oportunidad de participar en proyectos de investigación y desarrollo')
        self.tabla.heading('EnfasisI', text='II.4 Énfasis que se le prestaba a la investigación dentro del proceso de enseñanza')
        self.tabla.heading('SatisfaccionE', text='II.6 Satisfacción con las condiciones de estudio (Infraestructura)')
        self.tabla.heading('ExperienciaR', text='II.7 Experiencia obtenida a través de la residencia profesional')
        self.tabla.heading('53', text='Actividad a la que se dedica actualmente')
        self.tabla.heading('54', text='En caso de trabajar: Tiempo Transcurrido para obtener el primer empleo')
        self.tabla.heading('55', text='Medio para Obtener el Empleo')
        self.tabla.heading('56', text='Requisitos de contratación')
        self.tabla.heading('57', text='Antigüedad en el empleo')
        self.tabla.heading('58', text='Ingreso (Salario mínimo diario)')
        self.tabla.heading('59', text='Nivel jerárquico en el trabajo')
        self.tabla.heading('60', text='Condición de trabajo')
        self.tabla.heading('61', text='Relación del trabajo con su área de formación')
        self.tabla.heading('62', text='Datos de la empresa u organismo')
        self.tabla.heading('63', text='Giro o actividad principal de la empresa u organismo')
        self.tabla.heading('64', text='Razón social')
        self.tabla.heading('65', text='Idiomas que utiliza en su trabajo  ')
        self.tabla.heading('66', text='En que proporción utiliza en el desempeño de sus actividades laborales cada una de las habilidades del idioma extranjero [Hablar]')
        self.tabla.heading('67', text='En que proporción utiliza en el desempeño de sus actividades laborales cada una de las habilidades del idioma extranjero [Escribir] ')
        self.tabla.heading('68', text='En que proporción utiliza en el desempeño de sus actividades laborales cada una de las habilidades del idioma extranjero [Leer] ')
        self.tabla.heading('69', text='En que proporción utiliza en el desempeño de sus actividades laborales cada una de las habilidades del idioma extranjero [Escuchar] ')
        self.tabla.heading('70', text='Calle')
        self.tabla.heading('71', text='Número')
        self.tabla.heading('72', text='Colonia')
        self.tabla.heading('73', text='Código Postal')
        self.tabla.heading('74', text='Ciudad')
        self.tabla.heading('75', text='Municipio')
        self.tabla.heading('76', text='Estado')
        self.tabla.heading('77', text='País ')
        self.tabla.heading('78', text='Teléfono Oficina')
        self.tabla.heading('79', text='Fax Oficina')
        self.tabla.heading('80', text='Correo Electrónico Laboral')
        self.tabla.heading('81', text='Página Web Laboral')
        self.tabla.heading('82', text='Nombre del jefe inmediato')
        self.tabla.heading('83', text='Puesto del jefe inmediato')
        self.tabla.heading('84', text='III.13 Sector Económico de la Empresa u Organización')
        self.tabla.heading('85', text='III.14 Tamaño de la empresa u organización')
        self.tabla.heading('86', text='IV.1 Eficiencia para realizar las actividades laborales, en relación con su formación académica')
        self.tabla.heading('87', text='IV.2	Cómo califica su formación académica con respecto a su desempeño laboral')
        self.tabla.heading('88', text='IV.3 Utilidad de las residencias profesionales o prácticas profesionales para su desarrollo laboral y profesionalla empresa')
        self.tabla.heading('89', text='1. Área o Campo de Estudio')
        self.tabla.heading('90', text='2. Titulación')
        self.tabla.heading('91', text='3. Experiencia Laboral/práctica (antes de egresar)')
        self.tabla.heading('92', text='4. Competencia Laboral: Habilidad para resolver problemas, capacidad de análisis, habilidad para el aprendizaje, creatividad, administración del tiempo, capacidad de negociación, habilidades manuales, trabajo en equipo, iniciativa, honestidad, persistencia, etc.')
        self.tabla.heading('93', text='5. Posicionamiento de la Institución de Egreso')
        self.tabla.heading('94', text='6. Conocimiento de Idiomas Extranjeros')
        self.tabla.heading('95', text='7. Recomendaciones/ referencias')
        self.tabla.heading('96', text='8. Personalidad/ Actitudes')
        self.tabla.heading('97', text='9. Capacidad de liderazgo')
        self.tabla.heading('98', text='10. Otros')
        self.tabla.heading('99', text='Le gustaría tomar cursos de actualización')
        self.tabla.heading('100', text='¿Qué curso de actualización le gustaría tomar?')
        self.tabla.heading('101', text='Le gustaría tomar algún Posgrado:')
        self.tabla.heading('102', text='¿Qué posgrado le gustaría tomar?')
        self.tabla.heading('103', text='VI.1 Pertenece a organizaciones sociales:')
        self.tabla.heading('104', text='Nombre de la organización(es) social(es) a la cual pertenece')
        self.tabla.heading('105', text='VI.2 Pertenece a organismos de profesionistas')
        self.tabla.heading('106', text='Nombre del organismo(s) de profesionistas al cual pertenece')
        self.tabla.heading('107', text='VI.3 Pertenece a la asociación de egresados')
        self.tabla.heading('108', text='Opinión o recomendación para mejorar la formación profesional de un egresado de su carrera')
        self.tabla.heading('109', text='Puntuación')
        
    

        # Iterar los datos combinados
        for i, egresado in enumerate(datos_combinados):
            matricula = egresado[0]
            correo = egresado[1]
            nombre = egresado[2]
            apellidop = egresado[3]
            apellidom = egresado[4]
            sexo = egresado[5]
            estadocivil = egresado[6]
            telefonocelular = egresado[7]
            telefonocasa = egresado[8]
            calle = egresado[9]
            numero = egresado[10]
            colonia = egresado[11]
            codigopostal = egresado[12]
            ciudad = egresado[13]
            municipio = egresado[14]
            estado = egresado[15]
            nombre_carrera = egresado[16]
            especialidad_egreso = egresado[17]
            añoegreso = egresado[18]
            mesegreso = egresado[19]
            dominioingles = egresado[20]
            dominiofrances = egresado[21]
            dominioitaliano = egresado[22]
            dominioaleman = egresado[23]
            dominiojapones = egresado[24]
            dominioword = egresado[25]
            dominioexcel = egresado[26]
            dominiopowerpoint = egresado[27]
            dominioaccess = egresado[28]
            dominiowindows = egresado[29]
            dominiolinux = egresado[30]
            dominiosolid = egresado[31]
            dominioautocad = egresado[32]
            dominionoi = egresado[33]
            dominiocoi = egresado[34]
            dominiobancos = egresado[35]
            certificaciones = egresado[36]
            tmaestria = egresado[37]
            nmaestria = egresado[38]
            imaestria = egresado[39]
            pmaestria = egresado[40]
            aingreso = egresado[41]
            sacademica = egresado[42]
            tieneD = egresado[43]
            nombreD = egresado[44]
            institucionD = egresado[45]
            Ingreso = egresado[46]
            situacionA = egresado[47]
            calidadD = egresado[48]
            planE = egresado[49]
            oportunidadP = egresado[50]
            enfasisI = egresado[51]
            satisfaccionE = egresado[52]
            experienciaR = egresado[53]
            actividadD = egresado[54]
            TiempoParaEmpleo = egresado[55]
            MediosEmpleo = egresado[56]
            Requisitosdecontratacion = egresado[57]
            AntiguedadEmpleo = egresado[58]
            Ingreso2 = egresado[59]
            NivelJerarquico = egresado[60]
            CondicionTrabajo = egresado[61]
            RelacionTrabajo = egresado[62]
            DatosEmpresa = egresado[63]
            GiroActividadEmpresa = egresado[64]
            RazonSocial  = egresado[65]
            IdiomaUT  = egresado[66]
            UtilizaIHablar  = egresado[67]
            UtilizaIEscribir  = egresado[68]
            UtilizaILeer  = egresado[69]
            UtilizaIEscuchar  = egresado[70]
            Calle2  = egresado[71]
            Numero2  = egresado[72]
            Colonia2  = egresado[73]
            CodigoPostal2  = egresado[74]
            Ciudad2  = egresado[75]
            Municipio2  = egresado[76]
            Estado2  = egresado[77]
            Pais2  = egresado[78]
            TelefonoOficina  = egresado[79]
            FaxOficina = egresado[80]
            CorreoLaboral  = egresado[81]
            PaginaWebLaboral  = egresado[82]
            Nombredeljefeinmediato  = egresado[83]
            Puestodeljefe  = egresado[84]
            SectorEconomico  = egresado[85]
            tamano  = egresado[86]
            eficienciaA  = egresado[87]
            calificaformacion  = egresado[88]
            utilidadresidencia  = egresado[89]
            areaocampo  = egresado[90]
            titulacion  = egresado[91]
            experiencialaboral  = egresado[92]
            competencialaboral  = egresado[93]
            posicionamientoI  = egresado[94]
            conocimientosI  = egresado[95]
            recomendaciones  = egresado[96]
            personalidad  = egresado[97]
            capacidadliderazgo  = egresado[98]
            otros  = egresado[99]
            tomarcursos  = egresado[100]
            cursosactuali  = egresado[101]
            tomarposgrado  = egresado[102]
            queposgrado  = egresado[103]
            perteneceOS  = egresado[104]
            nombreOrganizacion  = egresado[105]
            perteneceOP  = egresado[106]
            nombreOrganismo  = egresado[107]
            pertenecealaA  = egresado[108]
            Opiniones  = egresado[109]
            Puntuacion  = egresado[110]


           
          

            self.tabla.insert('', 'end', text=str(i+1), values=(matricula, correo, nombre, apellidop, apellidom,
                                                            sexo, estadocivil, telefonocelular, telefonocasa,
                                                            calle, numero, colonia, codigopostal, ciudad,
                                                            municipio, estado, nombre_carrera, especialidad_egreso,
                                                            añoegreso, mesegreso, dominioingles, dominiofrances, 
                                                            dominioitaliano, dominioaleman, dominiojapones, dominioword, dominioexcel,
                                                            dominiopowerpoint, dominioaccess,dominiowindows, dominiolinux, dominiosolid, dominioautocad, dominionoi,
                                                            dominiocoi, dominiobancos, certificaciones,tmaestria, nmaestria, imaestria, pmaestria,
                                                            aingreso, sacademica, tieneD, nombreD, institucionD, Ingreso, situacionA, calidadD, planE,
                                                            oportunidadP, enfasisI, satisfaccionE, experienciaR, actividadD, TiempoParaEmpleo,MediosEmpleo,
                                                            Requisitosdecontratacion, AntiguedadEmpleo, Ingreso2, NivelJerarquico, CondicionTrabajo, RelacionTrabajo,
                                                            DatosEmpresa, GiroActividadEmpresa, RazonSocial, IdiomaUT, UtilizaIHablar, UtilizaIEscribir, UtilizaILeer, 
                                                            UtilizaIEscuchar, Calle2, Numero2, Colonia2, CodigoPostal2, Ciudad2, Municipio2, Estado2,
                                                            Pais2, TelefonoOficina, FaxOficina, CorreoLaboral, PaginaWebLaboral, Nombredeljefeinmediato,
                                                            Puestodeljefe, SectorEconomico, tamano, eficienciaA, calificaformacion, utilidadresidencia,
                                                            areaocampo, titulacion, experiencialaboral, competencialaboral, posicionamientoI, conocimientosI,
                                                            recomendaciones, personalidad, capacidadliderazgo, otros, tomarcursos, cursosactuali, tomarposgrado,
                                                            queposgrado, perteneceOS, nombreOrganizacion, perteneceOP, nombreOrganismo, pertenecealaA, Opiniones,
                                                            Puntuacion))

            
            
        self.grid_rowconfigure(4, weight=1)  # Aumenta el tamaño de la fila 4
        self.grid_columnconfigure(0, weight=1)  # Aumenta el tamaño de la columna 0

        self.boton_editar = tk.Button(self, text="Editar")
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#39CF09',
                                cursor='hand2', activebackground='#38D506')
        self.boton_editar.grid(row=6, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_registro)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                   fg='#DAD5D6', bg='#C70039',
                                   cursor='hand2', activebackground='#EC0707')
        self.boton_eliminar.grid(row=6, column=1, padx=10, pady=10)

        self.boton_grafica = tk.Button(self, text="Generar Grafica", command=self.generar_graficas)
        self.boton_grafica.config(width=20, font=('Arial', 12, 'bold'),
                                  fg='#DAD5D6', bg='#00FFFF',
                                  cursor='hand2', activebackground='#00FFFF')
        self.boton_grafica.grid(row=6, column=2, padx=10, pady=10)

        self.grid_rowconfigure(4, minsize=50)
        self.grid_rowconfigure(5, weight=1)
        ladoy.grid(column=4, row=4, rowspan=2, sticky='ns')

    def realizar_busqueda(self, event=None):
        texto_busqueda = self.entry_busqueda.get()
       
        resultados = buscar(texto_busqueda)

    # Borrar las filas actuales de la tabla
        self.tabla.delete(*self.tabla.get_children())

    # Insertar los resultados de búsqueda en la tabla
        for i, p in enumerate(resultados):
            self.tabla.insert('', 'end', text=str(i+1), values=(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], 
                                                                p[11], p[12], p[13], p[14], p[15], p[16], p[17], p[18], p[19], p[20], 
                                                                p[21], p[22], p[23], p[24], p[25], p[26], p[27], p[28], p[29], p[30], 
                                                                p[31], p[32], p[33], p[34], p[35], p[36], p[37], p[38], p[39], p[40], 
                                                                p[41], p[42], p[43], p[44], p[45], p[46], p[47], p[48], p[49], p[50], 
                                                                p[51], p[52], p[53], p[54], p[55], p[56], p[57], p[58], p[59], p[60], 
                                                                p[61], p[62], p[63], p[64], p[65], p[66], p[67], p[68], p[69], p[70], 
                                                                p[71], p[72], p[73], p[74], p[75], p[76], p[77], p[78], p[79], p[80], 
                                                                p[81], p[82], p[83], p[84], p[85], p[86], p[87], p[88], p[89], p[90], 
                                                                p[91], p[92], p[93], p[94], p[95], p[96], p[97], p[98], p[99], p[100], 
                                                                p[101], p[102], p[103], p[104], p[105], p[106], p[107], p[108], p[109], p[110]))
