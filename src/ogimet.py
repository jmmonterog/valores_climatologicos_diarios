from datetime import datetime
from datetime import date
from observacion import observacion
from utilidad import utilidad
from bs4 import BeautifulSoup
import calendar
from conexion import conexion
from url import url


class ogimet:
    """
    Clase que encapsula las funcionalidades para hacer webscraping desde ogimet
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def busca_tabla(self):
        tabla = self.soup.find('table', {'align': 'center', 'border': "0", 'cellspacing': "1", 'bgcolor': '#d0d0d0'})
        return tabla

    def obtiene_campos(self):
        tabla = self.busca_tabla()
        # procesa_fecha
        if tabla is not None:
            cabecera = tabla.find_all('caption')[0]
            fecha_txt = cabecera.find_all('b')[2].string
            self.fecha = datetime.strptime(fecha_txt, '%Y/%m/%d')
            # procesa campos
            cab_tabla = tabla.find_all('thead')[0]
            filas_cab_tabla = cab_tabla.find_all('tr')
            misclaves = []
            for fila in filas_cab_tabla:
                celditas = fila.find_all('th')
                for celdita in celditas:
                    clave = celdita.text.strip()
                    if clave.startswith("No hay datos"):
                        return misclaves
                    else:
                        misclaves.append(celdita.text.strip())

            if "Max" in misclaves:
                index = misclaves.index("Max")
                misclaves.pop(index)
                if "Temperatura(C)" in misclaves:
                    index = misclaves.index("Temperatura(C)")
                    misclaves.insert(index + 1, 'Temperatura(C)_Max')

            if "Min" in misclaves:
                index = misclaves.index("Min")
                misclaves.pop(index)
                if "Temperatura(C)" in misclaves:
                    index = misclaves.index("Temperatura(C)")
                    misclaves.insert(index + 2, 'Temperatura(C)_Min')

            if "Med" in misclaves:
                index = misclaves.index("Med")
                misclaves.pop(index)
                if "Temperatura(C)" in misclaves:
                    index = misclaves.index("Temperatura(C)")
                    misclaves.insert(index + 3, 'Temperatura(C)_Med')

            if "Temperatura(C)" in misclaves:
                index = misclaves.index("Temperatura(C)")
                misclaves.pop(index)

            if 'Dir.' in misclaves:
                index = misclaves.index('Dir.')
                misclaves.pop(index)
                if "Viento(km/h)" in misclaves:
                    index = misclaves.index("Viento(km/h)")
                    misclaves.insert(index + 1, 'Viento(km/h)_Dir.')

            if 'Vel.' in misclaves:
                index = misclaves.index('Vel.')
                misclaves.pop(index)
                if "Viento(km/h)" in misclaves:
                    index = misclaves.index("Viento(km/h)")
                    misclaves.insert(index + 2, 'Viento(km/h)_Vel.')

            if 'Rch.' in misclaves:
                index = misclaves.index('Rch.')
                misclaves.pop(index)
                if "Viento(km/h)" in misclaves:
                    index = misclaves.index("Viento(km/h)")
                    misclaves.insert(index + 3, 'Viento(km/h)_Rch.')

            if "Viento(km/h)" in misclaves:
                index = misclaves.index("Viento(km/h)")
                misclaves.pop(index)
            else:
                pass
        else:
            misclaves = []

        return (misclaves)

    def busca_filas(self):
        tabla = self.busca_tabla()
        # procesa_fecha
        if tabla is not None:
            cabecera = tabla.find_all('caption')[0]
            fecha_txt = cabecera.find_all('b')[2].string
            self.fecha = datetime.strptime(fecha_txt, '%Y/%m/%d')
            # procesa campos
            cab_tabla = tabla.find_all('thead')[0]
            filas = tabla.find_all('tr')
        else:
            filas = []
        return filas

    def procesa_filas(self, cabeceras, filas, estacion):
        # fijo fila
        lista = []
        for fila in filas[2:]:
            lista.append(self.procesa_fila(fila, self.fecha, cabeceras, estacion))
        return lista

    def procesa_fila(self, fila, fechaEntera, cabeceras, estacion):
        # patron para variables numericas
        pattern = '([0-9]+\.[0-9]+)'
        celdas = fila.find_all('td')
        # procesamiento de cada celda
        # creo la instancia de observacion
        registroDiario = observacion()
        registroDiario.indicativo = estacion
        for i in range(len(celdas)):
            if i == 0:
                fechaStr = celdas[0].find_all('a')[0].string
                mes = int(fechaStr.split('/')[1])
                anio = int(fechaEntera.year)
                mes = int(fechaEntera.month)
                dia = int(fechaStr.split('/')[0])
                fechaRegistro = date(anio, mes, dia)
                registroDiario.cambiarValor(cabeceras[0], fechaRegistro)

            else:
                if cabeceras[i] == 'Diariometeorológico':
                    break
                else:
                    contenido = celdas[i].find('font')
                    if contenido is not None:
                        registroDiario.cambiarValor(cabeceras[i], contenido.string)
        return registroDiario



