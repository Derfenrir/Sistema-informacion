from .conexion import DataBase
from tkinter import messagebox


def obtener_datos_combinados():
    conexion = DataBase()

    datos_combinados = []
    sql = '''
    SELECT Egresados.Matricula, Egresados.DireccionCorreoElectronico, Egresados.Nombre, Egresados.ApellidoPaterno, Egresados.ApellidoMaterno, Egresados.Sexo, Egresados.EstadoCivil, 
    Egresados.TelefonoCelular, Egresados.TelefonoCasa, DireccionEgresado.Calle, DireccionEgresado.Numero, DireccionEgresado.Colonia, DireccionEgresado.CodigoPostal, 
    DireccionEgresado.Ciudad, DireccionEgresado.Municipio, DireccionEgresado.Estado, Carreras.NombreCarrera, Informacionegreso.EspecialidadDeEgreso, Informacionegreso.AñoDeEgreso, 
    Informacionegreso.MesDeEgreso, DominioIdioma.DominioIdiomaIngles, DominioIdioma.DominioIdiomaFrances, DominioIdioma.DominioIdiomaItaliano, DominioIdioma.DominioIdiomaAleman,
    DominioIdioma.DominioIdiomaJapones, DominioPaquete.DominioPaqueteWord, DominioPaquete.DominioPaqueteExcel, DominioPaquete.DominioPaquetePowerPoint, DominioPaquete.DominioPaqueteAccess, DominioPaquete.DominioPaqueteWindows,
    DominioPaquete.DominioPaqueteLinux, DominioPaquete.DominioPaqueteSolidworks, DominioPaquete.DominioPaqueteAutocad, DominioPaquete.DominioPaqueteAspelNOI, DominioPaquete.DominioPaqueteAspelCOI,
    DominioPaquete.DominioPaqueteAspelBancos, Maestria.Certificaciones, Maestria.TieneMaestria, Maestria.NombreMaestria, Maestria.InstitucionMaestria, Maestria.PaisMaestria, Maestria.AnoIngreso, 
    Maestria.SituacionAcademica, Doctorado.TieneDoctorado, Doctorado.NombreDoctorado, Doctorado.InstitucionDoctorado, Doctorado.AnoIngreso2, Doctorado.SituacionAcademica, PertinenciayDisponibilidad.CalidadDocentes,
    PertinenciayDisponibilidad.PlanEstudio, PertinenciayDisponibilidad.OportunidadProyecto, PertinenciayDisponibilidad.EnfasisInvestigacion, PertinenciayDisponibilidad.SatisfaccionEstudio, 
    PertinenciayDisponibilidad.ExperienciaResidencia, EmpleoEgresado.ActividadDedica, EmpleoEgresado.TiempoParaEmpleo, EmpleoEgresado.MediosEmpleo, EmpleoEgresado.Requisitosdecontratacion, EmpleoEgresado.AntiguedadEmpleo, 
    EmpleoEgresado.Ingreso, EmpleoEgresado.NivelJerarquico, EmpleoEgresado.CondicionTrabajo, EmpleoEgresado.RelacionTrabajo, EmpleoEgresado.DatosEmpresa, EmpleoEgresado.GiroActividadEmpresa, EmpleoEgresado.RazonSocial,
    IdiomaTrabajo.IdiomaUtilizaTrabajo, IdiomaTrabajo.UtilizaIdioma_Hablar, IdiomaTrabajo.UtilizaIdioma_Escribir, IdiomaTrabajo.UtilizaIdioma_Leer, IdiomaTrabajo.UtilizaIdioma_Escuchar, DomicilioLaboral.Calle2, 
    DomicilioLaboral.Numero2, DomicilioLaboral.Colonia2, DomicilioLaboral.CodigoPostal2, DomicilioLaboral.Ciudad2, DomicilioLaboral.Municipio2, DomicilioLaboral.Estado2, DomicilioLaboral.Pais2, DomicilioLaboral.TelefonoOficina, 
    DomicilioLaboral.FaxOficina, DomicilioLaboral.CorreoLaboral, DomicilioLaboral.PaginaWebLaboral, DomicilioLaboral.Nombredeljefeinmediato, DomicilioLaboral.Puestodeljefeinmediato, DomicilioLaboral.SectorEconomicodelaEmpres, 
    DomicilioLaboral.Tamano, DesempeñoaLaboral.Eficienciarealizaracti, DesempeñoaLaboral.Calificasuformacionac, DesempeñoaLaboral.Utilidaddelasresidencia, AspectosContratacion.Area_o_Campo_de_Estudio, AspectosContratacion.Titulacion, 
    AspectosContratacion.Experiencia_Laboral_practica_ante, AspectosContratacion.Competencia_Laboral_Habilidad_para, AspectosContratacion.Posicionamiento_de_la_Institucion, AspectosContratacion.Conocimiento_de_Idiomas_Extranjeros, 
    AspectosContratacion.Recomendaciones_referencias, AspectosContratacion.Personalidad_Actitudes, AspectosContratacion.Capacidad_de_liderazgo, AspectosContratacion.Otros, ActualizacionConocimientos.Le_gustaria_tomar_cursos_de_actu,
    ActualizacionConocimientos.Que_curso_de_actualizacion_le_gustar, ActualizacionConocimientos.Le_gustaria_tomar_algun_Posgrado, ActualizacionConocimientos.Que_posgrado_le_gustaria_tomar, ParticipacionSocial.Pertenece_a_organizaciones_sociales,
    ParticipacionSocial.Nombre_de_la_organizacion, ParticipacionSocial.Pertenece_a_organismos_de_profesionistas, ParticipacionSocial.Nombre_del_organismo_s_de_profesi, ParticipacionSocial.Pertenece_a_la_asociacion_de, 
    ComentariosSugerencias.Opinionesorecomendaciones, ComentariosSugerencias.Puntuacion
    FROM Egresados
    LEFT JOIN DireccionEgresado ON Egresados.Matricula = DireccionEgresado.Matricula
    LEFT JOIN Informacionegreso ON Egresados.Matricula = Informacionegreso.Matricula
    LEFT JOIN Carreras ON Informacionegreso.CarreraId = Carreras.CarreraId
    LEFT JOIN DominioIdioma ON Egresados.Matricula = DominioIdioma.Matricula 
    LEFT JOIN DominioPaquete ON Egresados.Matricula = DominioPaquete.Matricula
    LEFT JOIN Maestria ON Egresados.Matricula = Maestria.Matricula
    LEFT JOIN Doctorado ON Egresados.Matricula = Doctorado.Matricula
    LEFT JOIN PertinenciayDisponibilidad ON Egresados.Matricula = PertinenciayDisponibilidad.Matricula
    LEFT JOIN EmpleoEgresado ON Egresados.Matricula = EmpleoEgresado.Matricula
    LEFT JOIN IdiomaTrabajo ON EmpleoEgresado.Matricula = IdiomaTrabajo.Matricula
    LEFT JOIN DomicilioLaboral ON EmpleoEgresado.Matricula = DomicilioLaboral.Matricula
    LEFT JOIN DesempeñoaLaboral ON EmpleoEgresado.Matricula = DesempeñoaLaboral.Matricula 
    LEFT JOIN AspectosContratacion ON EmpleoEgresado.Matricula = AspectosContratacion.Matricula
    LEFT JOIN ActualizacionConocimientos ON Egresados.Matricula = ActualizacionConocimientos.Matricula
    LEFT JOIN  ParticipacionSocial ON Egresados.Matricula = ParticipacionSocial.Matricula
    LEFT JOIN ComentariosSugerencias ON Egresados.Matricula = ComentariosSugerencias.Matricula
    '''

    try:
        conexion.cursor.execute(sql)
        datos_combinados = conexion.cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener datos combinados: {str(e)}")
        datos_combinados = []  # Devolver una lista vacía en caso de error
    finally:
        conexion.cerrar()

    return datos_combinados


def buscar(texto_busqueda):
    conexion = DataBase()
    datos_combinados = []

    sql = f'''
    SELECT Egresados.Matricula, Egresados.DireccionCorreoElectronico, Egresados.Nombre, Egresados.ApellidoPaterno, Egresados.ApellidoMaterno, Egresados.Sexo, Egresados.EstadoCivil, 
    Egresados.TelefonoCelular, Egresados.TelefonoCasa, DireccionEgresado.Calle, DireccionEgresado.Numero, DireccionEgresado.Colonia, DireccionEgresado.CodigoPostal, 
    DireccionEgresado.Ciudad, DireccionEgresado.Municipio, DireccionEgresado.Estado, Carreras.NombreCarrera, Informacionegreso.EspecialidadDeEgreso, Informacionegreso.AñoDeEgreso, 
    Informacionegreso.MesDeEgreso, DominioIdioma.DominioIdiomaIngles, DominioIdioma.DominioIdiomaFrances, DominioIdioma.DominioIdiomaItaliano, DominioIdioma.DominioIdiomaAleman,
    DominioIdioma.DominioIdiomaJapones, DominioPaquete.DominioPaqueteWord, DominioPaquete.DominioPaqueteExcel, DominioPaquete.DominioPaquetePowerPoint, DominioPaquete.DominioPaqueteAccess, DominioPaquete.DominioPaqueteWindows,
    DominioPaquete.DominioPaqueteLinux, DominioPaquete.DominioPaqueteSolidworks, DominioPaquete.DominioPaqueteAutocad, DominioPaquete.DominioPaqueteAspelNOI, DominioPaquete.DominioPaqueteAspelCOI,
    DominioPaquete.DominioPaqueteAspelBancos, Maestria.Certificaciones, Maestria.TieneMaestria, Maestria.NombreMaestria, Maestria.InstitucionMaestria, Maestria.PaisMaestria, Maestria.AnoIngreso, 
    Maestria.SituacionAcademica, Doctorado.TieneDoctorado, Doctorado.NombreDoctorado, Doctorado.InstitucionDoctorado, Doctorado.AnoIngreso2, Doctorado.SituacionAcademica, PertinenciayDisponibilidad.CalidadDocentes,
    PertinenciayDisponibilidad.PlanEstudio, PertinenciayDisponibilidad.OportunidadProyecto, PertinenciayDisponibilidad.EnfasisInvestigacion, PertinenciayDisponibilidad.SatisfaccionEstudio, 
    PertinenciayDisponibilidad.ExperienciaResidencia, EmpleoEgresado.ActividadDedica, EmpleoEgresado.TiempoParaEmpleo, EmpleoEgresado.MediosEmpleo, EmpleoEgresado.Requisitosdecontratacion, EmpleoEgresado.AntiguedadEmpleo, 
    EmpleoEgresado.Ingreso, EmpleoEgresado.NivelJerarquico, EmpleoEgresado.CondicionTrabajo, EmpleoEgresado.RelacionTrabajo, EmpleoEgresado.DatosEmpresa, EmpleoEgresado.GiroActividadEmpresa, EmpleoEgresado.RazonSocial,
    IdiomaTrabajo.IdiomaUtilizaTrabajo, IdiomaTrabajo.UtilizaIdioma_Hablar, IdiomaTrabajo.UtilizaIdioma_Escribir, IdiomaTrabajo.UtilizaIdioma_Leer, IdiomaTrabajo.UtilizaIdioma_Escuchar, DomicilioLaboral.Calle2, 
    DomicilioLaboral.Numero2, DomicilioLaboral.Colonia2, DomicilioLaboral.CodigoPostal2, DomicilioLaboral.Ciudad2, DomicilioLaboral.Municipio2, DomicilioLaboral.Estado2, DomicilioLaboral.Pais2, DomicilioLaboral.TelefonoOficina, 
    DomicilioLaboral.FaxOficina, DomicilioLaboral.CorreoLaboral, DomicilioLaboral.PaginaWebLaboral, DomicilioLaboral.Nombredeljefeinmediato, DomicilioLaboral.Puestodeljefeinmediato, DomicilioLaboral.SectorEconomicodelaEmpres, 
    DomicilioLaboral.Tamano, DesempeñoaLaboral.Eficienciarealizaracti, DesempeñoaLaboral.Calificasuformacionac, DesempeñoaLaboral.Utilidaddelasresidencia, AspectosContratacion.Area_o_Campo_de_Estudio, AspectosContratacion.Titulacion, 
    AspectosContratacion.Experiencia_Laboral_practica_ante, AspectosContratacion.Competencia_Laboral_Habilidad_para, AspectosContratacion.Posicionamiento_de_la_Institucion, AspectosContratacion.Conocimiento_de_Idiomas_Extranjeros, 
    AspectosContratacion.Recomendaciones_referencias, AspectosContratacion.Personalidad_Actitudes, AspectosContratacion.Capacidad_de_liderazgo, AspectosContratacion.Otros, ActualizacionConocimientos.Le_gustaria_tomar_cursos_de_actu,
    ActualizacionConocimientos.Que_curso_de_actualizacion_le_gustar, ActualizacionConocimientos.Le_gustaria_tomar_algun_Posgrado, ActualizacionConocimientos.Que_posgrado_le_gustaria_tomar, ParticipacionSocial.Pertenece_a_organizaciones_sociales,
    ParticipacionSocial.Nombre_de_la_organizacion, ParticipacionSocial.Pertenece_a_organismos_de_profesionistas, ParticipacionSocial.Nombre_del_organismo_s_de_profesi, ParticipacionSocial.Pertenece_a_la_asociacion_de, 
    ComentariosSugerencias.Opinionesorecomendaciones, ComentariosSugerencias.Puntuacion
    FROM Egresados
    LEFT JOIN DireccionEgresado ON Egresados.Matricula = DireccionEgresado.Matricula
    LEFT JOIN Informacionegreso ON Egresados.Matricula = Informacionegreso.Matricula
    LEFT JOIN Carreras ON Informacionegreso.CarreraId = Carreras.CarreraId
    LEFT JOIN DominioIdioma ON Egresados.Matricula = DominioIdioma.Matricula 
    LEFT JOIN DominioPaquete ON Egresados.Matricula = DominioPaquete.Matricula
    LEFT JOIN Maestria ON Egresados.Matricula = Maestria.Matricula
    LEFT JOIN Doctorado ON Egresados.Matricula = Doctorado.Matricula
    LEFT JOIN PertinenciayDisponibilidad ON Egresados.Matricula = PertinenciayDisponibilidad.Matricula
    LEFT JOIN EmpleoEgresado ON Egresados.Matricula = EmpleoEgresado.Matricula
    LEFT JOIN IdiomaTrabajo ON EmpleoEgresado.Matricula = IdiomaTrabajo.Matricula
    LEFT JOIN DomicilioLaboral ON EmpleoEgresado.Matricula = DomicilioLaboral.Matricula
    LEFT JOIN DesempeñoaLaboral ON EmpleoEgresado.Matricula = DesempeñoaLaboral.Matricula 
    LEFT JOIN AspectosContratacion ON EmpleoEgresado.Matricula = AspectosContratacion.Matricula
    LEFT JOIN ActualizacionConocimientos ON Egresados.Matricula = ActualizacionConocimientos.Matricula
    LEFT JOIN  ParticipacionSocial ON Egresados.Matricula = ParticipacionSocial.Matricula
    LEFT JOIN ComentariosSugerencias ON Egresados.Matricula = ComentariosSugerencias.Matricula
    WHERE Egresados.Nombre LIKE '%{texto_busqueda}%' OR Egresados.Matricula LIKE '%{texto_busqueda}%' OR DireccionEgresado.Calle LIKE '%{texto_busqueda}%' OR DireccionEgresado.Numero LIKE '%{texto_busqueda}%' OR Informacionegreso.CarreraId LIKE '%{texto_busqueda}%' OR Carreras.NombreCarrera LIKE '%{texto_busqueda}%'
    '''

    try:
        conexion.cursor.execute(sql)
        datos_combinados = conexion.cursor.fetchall()
    except Exception as e:
        print(f"Error en la búsqueda: {str(e)}")
        datos_combinados = []  # Devolver una lista vacía en caso de error
    finally:
        conexion.cerrar()

    return datos_combinados

from .conexion import DataBase

def eliminar_egresado(matricula):
    conexion = DataBase()
    eliminado = False

    try:
        sql = f"DELETE FROM Egresados WHERE Matricula = '{matricula}'"
        conexion.cursor.execute(sql)
        conexion.connection.commit()
        eliminado = True
    except Exception as e:
        print(f"Error al eliminar el registro: {str(e)}")
    finally:
        conexion.cerrar()

    return eliminado

def obtener_idiomas():
    conexion = DataBase()

    idiomas = []

    try:
        sql = "SELECT Nombre FROM Idiomas"
        conexion.cursor.execute(sql)
        resultados = conexion.cursor.fetchall()

        for resultado in resultados:
            idioma = resultado[0]
            idiomas.append(idioma)

    except Exception as e:
        print(f"Error al obtener idiomas: {str(e)}")
    finally:
        conexion.cerrar()

    return idiomas

def obtener_dominios_egresado(matricula):
    conexion = DataBase()
    dominios = {}

    try:
        sql = '''
        SELECT Idiomas.Nombre, DominioIdioma.Dominio
        FROM DominioIdioma
        INNER JOIN Idiomas ON DominioIdioma.IdiomaId = Idiomas.IdiomaId
        WHERE DominioIdioma.Matricula = %s
        '''
        conexion.cursor.execute(sql, (matricula,))
        resultados = conexion.cursor.fetchall()

        for resultado in resultados:
            idioma = resultado[0]
            dominio = resultado[1]
            dominios[idioma] = dominio

    except Exception as e:
        print(f"Error al obtener los dominios del egresado: {str(e)}")

    finally:
        conexion.cerrar()

    return dominios

