import requests
import json
from observacion import observacion
import backoff

class openData:

    def __init__(self):
        self.__querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqbW9udGVyb2dAYWVtZXQuZXMiLCJqdGkiOiJiNzllNTAxNi1iZjRlLTQ2MjEtYjY4Mi0yZjZiNzg1NWY4NWIiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTY0NzYxOTAwNCwidXNlcklkIjoiYjc5ZTUwMTYtYmY0ZS00NjIxLWI2ODItMmY2Yjc4NTVmODViIiwicm9sZSI6IiJ9.O4toCAcY_dJmwiWnk7Tf-pYnRRy5jm8KSEimzWa_wS4"}
        self.__headers = {'cache-control': "no-cache"}

    @backoff.on_exception(backoff.expo,
                          requests.exceptions.RequestException,
                          max_tries=8,
                          jitter=None)
    def obten_conexion_datos(self, fini, ffin,estacion):
        #fini: AAAA-MM-DDT00:00:00UTC
        #ffin: AAAA-MM-DDT23:59:59UTC
        url="https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/"+fini+"/fechafin/"+ffin+"/estacion/"+estacion
        response = requests.request("GET", url, headers=self.__headers, params=self.__querystring)
        respuesta_API = json.loads(response.text)
        estado = respuesta_API["estado"]
        if estado == 200:
            url_datos = respuesta_API["datos"]
            return url_datos
        else:
            return None

    @backoff.on_exception(backoff.expo,
                          requests.exceptions.RequestException,
                          max_tries=8,
                          jitter=None)
    def obten_conexion_estaciones(self):
        url_estaciones = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones"
        response = requests.request("GET", url_estaciones, headers=self.__headers, params=self.__querystring)
        respuesta_API = json.loads(response.text)
        estado = respuesta_API["estado"]
        if estado == 200:
            url_datos = respuesta_API["datos"]
            return url_datos
        else:
            return None

    def obten_datos(self,url):
        response = requests.request("GET", url, headers=self.__headers, params=self.__querystring)
        return json.loads(response.text)

    def procesa_datos(self,datos):
        listado = []
        for dato in datos:
            registroDiario = observacion()
            if 'indicativo' in dato.keys():
                registroDiario.indicativo = dato['indicativo']
            if 'fecha' in dato.keys():
                registroDiario.fecha=dato['fecha']
            if 'tmax' in dato.keys():
                registroDiario.tempMax = dato['tmax']
            if 'tmin' in dato.keys():
                registroDiario.tempMin = dato['tmin']
            if 'tmed' in dato.keys():
                registroDiario.tempMed = dato['tmed']
            if 'prec' in dato.keys():
                registroDiario.precipitacion = dato['prec']
            if 'dir' in dato.keys():
                registroDiario.dir = self.codifica_dir_viento(dato['dir'])
            if 'velmedia' in dato.keys():
                registroDiario.vel = dato['velmedia']
            if 'racha' in dato.keys():
                registroDiario.racha = dato['racha']
            if 'sol' in dato.keys():
                registroDiario.sol = dato['sol']
            listado.append(registroDiario)
        return listado


    def obten_estaciones(self,datos):
        estaciones = []
        for dato in datos:
            if dato['indsinop']=='':
                estaciones.append(dato['indicativo'])
        return estaciones


    def obten_registros_diarios(self,fini,ffin):
        '''
        Método que permite obtener los registros diarios de todas las estaciones entre las fechas indicadas
        Parametro: fini: fecha y hora inicial (AAAA-MM-DDTHH:MM:SSUTC)
        Parametro: fini: fecha y hora final (AAAA-MM-DDTHH:MM:SSUTC)
        '''
        resultados = []
        for estacion in self.obten_estaciones(self.obten_datos(self.obten_conexion_estaciones())):
            url_datos = self.obten_conexion_datos(fini, ffin, estacion)
            if url_datos is None:
                continue
            else:
                lista_datos = self.obten_datos(url_datos)
                for registroDiario in self.procesa_datos(lista_datos):
                    resultados.append(registroDiario.clave_valor)
        return resultados

    def codifica_dir_viento(self,dato):
        datonum = float(dato)
        if (350 <= datonum <= 10):
            return "N"
        elif (10 < datonum < 35):
            return "NNE"
        elif (35 <= datonum <= 55):
            return "NE"
        elif (55 < datonum < 80):
            return "ENE"
        elif (80 <= datonum <= 100):
            return "E"
        elif (100 < datonum < 125):
            return "ESE"
        elif (125 <= datonum <= 145):
            return "SE"
        elif (145 < datonum < 170):
            return "SSE"
        elif (170 <= datonum <= 190):
            return "S"
        elif (190 < datonum < 215):
            return "SSW"
        elif (215 <= datonum <= 235):
            return "SW"
        elif (235 < datonum < 260):
            return "WSW"
        elif (260 <= datonum <= 280):
            return "W"
        elif (280 < datonum < 305):
            return "WNW"
        elif (305 <= datonum <= 325):
            return "NW"
        else:
            return "NNW"









