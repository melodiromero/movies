import pandas as pd
import numpy as np
import datetime as dt

# Se importa el dataset de trabajo
df = pd.read_csv('./dataset/dataset_limpio.csv', delimiter=',')

def obtenerMesComoNro(mes):
    """ obtenerMesComoNro recibe un parámetro tipo cadena o string y retorna el correspondiente mes en número.
    """
    # Se valida que el parametro recibido sea un string.
    #falta
    m = {
        'enero':        1,
        'febrero':      2,
        'marzo':        3,
        'abril':        4,
        'mayo':         5,
        'junio':        6,
        'julio':        7,
        'agosto':       8,
        'septiembre':   9,
        'octubre':      10,
        'noviembre':    11,
        'diciembre':    12
    }

    # Ahora, se valida que el parámetro recibido sea una clave en el diccionario m.
    if mes in m:
        return m[mes]
    else: 
        return 0


def Leer_cantidad_filmaciones_mes(mes):
    """ Leer_cantidad_filmaciones_mes recibe el parámetro mes tipo cadena o string, 
        consulta al método obtenerMesComoNro que nro mes es y recupera del dataframe los registros, 
        cuya pelicula se estrenaron en dicho mes.
        La función retorna un numero: 0 en casos de error o el total (en numero) de peliculas estrenadas en el mes solicitado.
    """
    nromes = obtenerMesComoNro(mes)

    if nromes == 0:
        return 0
    else: 
        return df[df['release_month'] == nromes].shape[0]

""" pruebas...

print('enero', Leer_cantidad_filmaciones_mes('enero'))

print('febrero', Leer_cantidad_filmaciones_mes('febrero'))

print('marzo', Leer_cantidad_filmaciones_mes('marzo'))

print('abril',Leer_cantidad_filmaciones_mes('abril'))

print('mayo',Leer_cantidad_filmaciones_mes('mayo'))

print('junio', Leer_cantidad_filmaciones_mes('junio'))

print('julio', Leer_cantidad_filmaciones_mes('julio'))

print('agosto', Leer_cantidad_filmaciones_mes('agosto'))

print('septiembre', Leer_cantidad_filmaciones_mes('septiembre'))

print('octubre', Leer_cantidad_filmaciones_mes('octubre'))

print('noviembre', Leer_cantidad_filmaciones_mes('noviembre'))

print('diciembre', Leer_cantidad_filmaciones_mes('diciembre'))

"""