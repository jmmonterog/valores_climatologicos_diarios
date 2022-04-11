# Práctica 1 de Tipología y Ciclo de Vida de los Datos.
# Cargamos las librerías.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Indicativo:
    '''
    Clase que encapsula la funcionalidad relativa a la obtención de indicativos
    '''


    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-extensions')
        # Opciones de navegación usando Google Chrome
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-extensions')
        self.driver_path= 'C:\\Users\\jmont\\Documents\\Tipologia_ejecutar\\chromedriver.exe'
        self.driver = webdriver.Chrome(self.driver_path)
        # Iniciar el driver en la pantalla
        self.driver.set_window_position(2000, 0)
        self.driver.maximize_window()
        time.sleep(1)


    def busqueda_tabla(self):
        # Inicializamos la navegación en Google Chrome dentro de nuestra web.
        self.driver.get('https://www.ogimet.com/indicativos.phtml')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td[2]/form/center/table/tbody/tr/td[1]/input'))).click()
        # Convertimos el objeto HTML en una lista\n",
        texto = self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[2]/table/tbody')
        texto = texto.text
        # Cortamos los elementos por el salto de carro
        texto = texto.split('\n')
        return texto

    def filtrado(self,pais,texto):
        # "\"\"\" Filtramos por el Pais objetivo.\n",
        # "    Args:\n",
        # "        Pais -- Nombre del pais en Ingles como string.\n",
        # "    Returns:\n",
        # "        Listado de los indicadores.\n",
        # "    \"\"\"\n",
        pais_match = list(filter(lambda x: pais in x, texto))
        # Iteramos para extraer sólo los indicadores únicos de ogimet.\n",
        indicadores = []
        for i in pais_match:
            if (i[0:5] != "----"):
                indicadores.append(i[0:5])
                indicadores_unicos = set(indicadores)
        return indicadores_unicos


