from observacion import observacion
import csv

class utilidad:


    def month_year_iter(start_month, start_year, end_month, end_year):
        ym_start = 12 * start_year + start_month - 1
        ym_end = 12 * end_year + end_month
        for ym in range(ym_start, ym_end):
            y, m = divmod(ym, 12)
            yield y, m + 1

    def escribe_fichero(valores_registros, ruta_salida):
        miObs = observacion()
        print(list(miObs.claves))
        try:
            with open(ruta_salida+'\\'+'datos.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=list(miObs.claves))
                writer.writeheader()
                for valores in valores_registros:
                    writer.writerow(valores)
        except IOError:
            print("I/O error")

