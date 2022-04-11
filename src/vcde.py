from utilidad import utilidad
import calendar
from url import url
from conexion import conexion
from ogimet import ogimet
from openData import openData
from indicativo import Indicativo
import logging
import sys


class VCDE:

    def __init__(self,anioini, mesini, aniofin, mesfin,ruta_salida='C:\\Users\\jmont\\Documents\\VCDE\\', ruta_logs='C:\\Users\\jmont\\Documents\\VCDE\\'):
        # obtención de los parámetros
        self.__anioini = anioini
        self.__mesini = mesini
        self.__aniofin = aniofin
        self.__mesfin = mesfin
        self.__ruta_salida = ruta_salida
        self.__rula_logs=ruta_logs

        # Creación y configuración del logger
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(ruta_logs + '\\' + 'VCDE.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )

        # Creación del objeto logger
        self.__logger = logging.getLogger()

        # Fijación del nivel de logging
        self.__logger.setLevel(logging.DEBUG)


    def obtencion_registros_diarios(self):


        self.__logger.info("INICIO de la ejecución de VCDE")

        # obtención indicativos sinópticos de España desde OGIMET
        self.__logger.info("INICIO de la obtención de los indicativos sinópticos de España desde OGIMET")
        indicativo = Indicativo()
        tabla = indicativo.busqueda_tabla()
        lestaciones = indicativo.filtrado("Spain", tabla)
        self.__logger.info("INICIO de la obtención de los indicativos sinópticos de España desde OGIMET")


        # acceso a OGIMET para obtención de datos de las estaciones que están en la lista lindicativos
        self.__logger.info("INICIO de los datos meteorológicos de las estaciones con indicativos sinópticos desde OGIMET")
        listado = []
        util = utilidad()
        for estacion in lestaciones:
           #print("voy por " + estacion.mostrar())
            for year, month in utilidad.month_year_iter(self.__mesini, self.__anioini, self.__mesfin, self.__aniofin):
                self.__logger.info("INICIO recuperación de datos de estación con indicativo sinóptico " + estacion + " desde OGIMET")
                x, y = calendar.monthrange(year, month)
                miURL = url(estacion, year, month, y)
                miconexion = conexion(miURL.url)
                elemento = ogimet(miconexion.contenido)
                #tabla = elemento.busca_tabla()
                campos = elemento.obtiene_campos()
                filas = elemento.busca_filas()
                registros = elemento.procesa_filas(campos, filas, estacion)
                registros.reverse()
                listado =  listado + registros
                self.__logger.info("FIN recuperación de datos de estación con indicativo sinóptico " + estacion + " desde OGIMET")


        valores_registros = [ registro.clave_valor for registro in listado]
        self.__logger.info("FIN de los datos meteorológicos de las estaciones con indicativos sinópticos desde OGIMET")


        #acceso a AEMET OpenData
        self.__logger.info("INICIO de los datos meteorológicos de las estaciones con indicativos sin indicativos sinópticos desde OGIMET")
        opendata = openData()
        diahoraIni = str(self.__anioini)+"-"+str(self.__mesini)+"-01T00:00:00UTC"
        x, y = calendar.monthrange(self.__aniofin, self.__mesfin)
        diahoraFin = str(self.__aniofin) + "-" +str(self.__mesfin) + "-" +str(y)+ "T23:59:59UTC"
        valores_registros = valores_registros + opendata.obten_registros_diarios(diahoraIni, diahoraFin)

        #escribir al fichero
        utilidad.escribe_fichero(valores_registros,self.__ruta_salida)
        self.__logger.info("FIN de los datos meteorológicos de las estaciones con indicativos sin indicativos sinópticos desde OGIMET")
        self.__logger.info("FIN de la ejecución de VCDE")


