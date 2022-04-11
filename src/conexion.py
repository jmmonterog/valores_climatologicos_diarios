import requests
import backoff

class conexion:
    '''
    Clase que encapsula a funcionalidad de conexión a los diferentes sitios web de los que vamos
    a hacer webscraping
    '''

    @backoff.on_exception(backoff.expo,
                          requests.exceptions.RequestException,
                          max_tries=8,
                          jitter=None)
    def __init__(self, url):
        self.page = requests.get(url)

    @property
    def contenido(self):
        return self.page.content

    @property
    def estado(self):
        return self.page.status_code
