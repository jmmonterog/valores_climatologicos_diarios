import calendar

class url:
    def __init__(self, indicativo, anio, mes, dia):
        self.indicativo = indicativo
        self.anio = anio
        self.mes = mes
        self.dia = dia

    @property
    def url(self):
        obj = calendar.Calendar()
        x, y = calendar.monthrange(self.anio, self.mes)
        return 'https://www.ogimet.com/cgi-bin/gsynres?ind=' + self.indicativo + '&ndays=' +str(y)+'&ano=' + str(
            self.anio) + '&mes=' + str(self.mes) + '&day=' + str(self.dia) + '&hora=23&ord=REV&enviar=Ver'
