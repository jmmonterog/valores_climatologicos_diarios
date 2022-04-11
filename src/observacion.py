class observacion:

    def __init__(self):
        self.__valores={}
        self.__valores['Indicativo'] = None
        self.__valores['Fecha']=None
        self.__valores['Temperatura(C)_Max']=None
        self.__valores['Temperatura(C)_Min']=None
        self.__valores['Temperatura(C)_Med']=None
        self.__valores['TdMed(C)']=None
        self.__valores['Hr.Med(%)']=None
        self.__valores['Viento(km/h)_Dir.']=None
        self.__valores['Viento(km/h)_Vel.']=None
        self.__valores['Viento(km/h)_Rch.']=None
        self.__valores['Prec.(mm)']=None
        self.__valores['Pres.n. mar(Hp)']=None
        self.__valores['Pres.n. est(Hp)']=None
        self.__valores['NubTotOct']=None
        self.__valores['NubbajOct'] = None
        self.__valores['VisKm'] = None
        self.__valores['SolD-1(h)'] = None
        self.__valores['Esp.Nie.(cm)'] = None
        self.__valores['Diariometeorológico'] = None

    @property
    def clave_valor(self):
        return self.__valores

    @property
    def valores(self):
        return self.__valores.values()

    @property
    def claves(self):
        return self.__valores.keys()

    def cambiarValor (self,key,valor):
        if key in self.__valores.keys():
            self.__valores[key]=valor
        else:
            #habria que lanzar excepcion
            pass
    @property
    def indicativo(self):
        return self.__valores['Indicativo']

    @indicativo.setter
    def indicativo(self, valor):
        self.__valores['Indicativo'] = valor

    @property
    def fecha(self):
        return self.__valores['Fecha']

    @fecha.setter
    def fecha(self, valor):
        self.__valores['Fecha'] = valor

    @property
    def tempMax(self):
        return self.__valores['Temperatura(C)_Max']

    @tempMax.setter
    def tempMax(self, valor):
        self.__valores['Temperatura(C)_Max'] = valor

    @property
    def tempMin(self):
        return self.__valores['Temperatura(C)_Min']

    @tempMin.setter
    def tempMin(self, valor):
        self.__valores['Temperatura(C)_Min'] = valor

    @property
    def tempMed(self):
        return self.__valores['Temperatura(C)_Med']

    @tempMed.setter
    def tempMed(self, valor):
        self.__valores['Temperatura(C)_Med'] = valor

    @property
    def tdMed(self):
        return self.__valores['TdMed(C)']

    @tdMed.setter
    def tdMed(self, valor):
        self.__valores['TdMed(C)'] = valor

    @property
    def hr(self):
        return self.__valores['Hr.Med(%)']

    @hr.setter
    def hr(self, valor):
        self.__valores['Hr.Med(%)'] = valor

    @property
    def vel(self):
        return self.__valores['Viento(km/h)_Vel.']

    @vel.setter
    def vel(self, valor):
        self.__valores['Viento(km/h)_Vel.'] = valor

    @property
    def dir(self):
        return self.__valores['Viento(km/h)_Dir.']

    @dir.setter
    def dir(self, valor):
        self.__valores['Viento(km/h)_Dir.'] = valor

    @property
    def racha(self):
        return self.__valores['Viento(km/h)_Rch.']

    @racha.setter
    def racha(self, valor):
        self.__valores['Viento(km/h)_Rch.'] = valor

    @property
    def precipitacion(self):
        return self.__valores['Prec.(mm)']

    @precipitacion.setter
    def precipitacion(self, valor):
        self.__valores['Prec.(mm)'] = valor

    @property
    def precipitacion(self):
        return self.__valores['Prec.(mm)']

    @precipitacion.setter
    def precipitacion(self, valor):
        self.__valores['Prec.(mm)'] = valor

    @property
    def sol(self):
        return self.__valores['SolD-1(h)']

    @precipitacion.setter
    def sol(self, valor):
        self.__valores['SolD-1(h)'] = valor

    def mostrar(self):
        cadena=""
        for key, value in self.__valores.items():
            cadena= cadena + key + ": " + str(value) + " "
        return cadena