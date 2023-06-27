import pandas as pd
import numpy as np
import datetime as dt

# Se importa el dataset de trabajo
df = pd.read_csv('./dataset/dataset_limpio.csv', delimiter=',')

# Declaración de estructuras de datos necesarios para los metodos.
# Diccionario de meses en español y su nro correspondiete.
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

# Diccionario de dias en español y su nro correspondiete.
d = {
    'lunes':        1,
    'martes':       2,
    'miercoles':    3,
    'jueves':       4,
    'viernes':      5,
    'sabado':       6,
    'domingo':      7
}

def ValidarMes(mes):
    if mes in m:
        return 1
    else:
        return 0
    
def ValidarDia(dia):
    if dia in d:
        return 1
    else:
        return 0

def Leer_cantidad_filmaciones_mes(mes: str):
    """ Leer_cantidad_filmaciones_mes recibe el parámetro mes tipo cadena o string, 
        y recupera del dataframe los registros, cuya pelicula se estrenaron en dicho mes.
        La función retorna un numero: 0 en casos de error o el total (en numero) de peliculas estrenadas en el mes solicitado.
    """
    return df[df['release_month'] ==  m[mes.lower()]].shape[0] 
    
    
def Leer_cantidad_filmaciones_dia(dia: str):
    """ Leer_cantidad_filmaciones_dia recibe el parámetro dia tipo cadena o string, 
        y recupera del dataframe los registros, cuya pelicula se estrenaron en dicho dia.
        La función retorna un numero: 0 en casos de error o el total (en numero) de peliculas estrenadas en el dia solicitado.
    """

    if type(dia)==str and dia in m:
        return df[df['release_month'] ==  m[dia]].shape[0] 
    else: 
        return 0    

def Leer_score_titulo(titulo: str):
    """ Leer_score_titulo recibe el parámetro titulo tipo cadena o string, 
        y recupera del dataframe, el título, el año de estreno y el score de la pelicula.
    """
    # Se valida que el parámetro titulo sea string y se encuentre en la columna title del el dataframe.
  
    resultado = []
    df1 = df[df['title'].astype(str) == titulo]
    # Se recorre en el caso que haya más de un registro.
    for i in range(len(df1)):
        resultado.append({  "titulo":       df1.iloc[i]['title'],
                            "anio" :        df1.iloc[i]['release_year'],
                            "popularidad":  df1.iloc[i]['popularity']
                        })
    
    return resultado

def Leer_votos_titulo(titulo: str):
    """ Se ingresa el título de una filmación esperando como respuesta el título, 
        la cantidad de votos y el valor promedio de las votaciones. 
        La misma variable deberá de contar con al menos 2000 valoraciones, 
        caso contrario, debemos contar con un mensaje avisando que no cumple esta condición
        y que por ende, no se devuelve ningun valor.
    """
    resultado = dict()
     
    df_nocumple = df[(df.title.astype(str) == titulo) & ( df.vote_count < 2000)]
    df_votos = df[(df.title.astype(str) == titulo) & ( df.vote_count >= 2000)]
    
    print(df_votos)

    if len(df_nocumple) == 0:
        return 1
    
    if len(df_votos) == 0:
        return 0
    else:
        # Se recorre en el caso que haya más de un registro.
        for i in range(len(df_votos)):
            resultado.append({  "titulo":       df_votos.iloc[i]['title'],
                                "anio" :        df_votos.iloc[i]['release_year'],
                                "voto_total":   df_votos.iloc[i]['vote_average'],
                                "voto_promedio":df_votos.iloc[i]['vote_count']
                            })
        
        return resultado

print(Leer_score_titulo("Sabrina"))

print(Leer_votos_titulo("Toy Story"))
""" # pruebas...

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

print('diciembre', Leer_cantidad_filmaciones_mes('hhhhh'))

print(Leer_score_titulo("Toy Story"))
"""