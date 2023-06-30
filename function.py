import pandas as pd
import datetime as dt
import ast
import json
from typing import Dict

# Se importa el dataset de trabajo
df      = pd.read_csv('./dataset/movies_limpio.csv', delimiter=',')
df_c    = pd.read_csv('./dataset/credits_limpio.csv', delimiter=',')
df_f    = pd.read_csv('./dataset/dataset_final.csv', delimiter=',')
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
    'lunes':        0,
    'martes':       1,
    'miercoles':    2,
    'jueves':       3,
    'viernes':      4,
    'sabado':       5,
    'domingo':      6
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

def extraer_nombre(nombre_columna):
    # Convierte el valor de la columna en un diccionario
    if pd.isna(nombre_columna):
        return None
    diccionario = ast.literal_eval(nombre_columna)
    # Extrae el valor de "name" si está presente en el diccionario
    if isinstance(diccionario, dict) and 'name' in diccionario:
        return diccionario['name']
    else:
        return None
    
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
    return df[df['release_day_of_week'] ==  d[dia.lower()]].shape[0] 
 

def Leer_score_titulo(titulo: str):
    """ Leer_score_titulo recibe el parámetro titulo tipo cadena o string, 
        y recupera del dataframe, el título, el año de estreno y el score de la pelicula.
    """
    # Se valida que el parámetro titulo sea string y se encuentre en la columna title del el dataframe.
    midicc = dict()
    midicc = df[df['title'].astype(str) == titulo]

    result = pd.DataFrame(midicc, columns=['title', 'release_year', 'popularity'])

    return result 
 

def Leer_votos_titulo(titulo: str):
    """ Se ingresa el título de una filmación esperando como respuesta el título, 
        la cantidad de votos y el valor promedio de las votaciones. 
        La misma variable deberá de contar con al menos 2000 valoraciones, 
        caso contrario, debemos contar con un mensaje avisando que no cumple esta condición
        y que por ende, no se devuelve ningun valor.
    """

    df_nocumple = df[(df.title.astype(str) == titulo) & ( df.vote_count < 2000)]
    df_votos = df[(df.title.astype(str) == titulo) & ( df.vote_count >= 2000)]
    
    if len(df_nocumple) != 0:
        return 1
    
    if len(df_votos) == 0:
        return 0
    else:
        # Se recorre en el caso que haya más de un registro.
        """for i in range(len(df_votos)):
            resultado    = {  "titulo":       df_votos.iloc[i]['title'],
                                 "anio" :        df_votos.iloc[i]['release_year'],
                                 "voto_total":   df_votos.iloc[i]['vote_average'],
                                 "voto_promedio":df_votos.iloc[i]['vote_count']
                            }
        print(type(resultado))"""
        # Crear un DataFrame con los datos de votos
        result = pd.DataFrame(df_votos, columns=['title', 'release_year', 'vote_average', 'vote_count'])

        return result
    

def Leer_get_actor(nombre_actor: str):
    ''' Se ingresa el nombre de un actor que se encuentre dentro del dataset debiendo devolver
        el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en 
        las que ha participado y el promedio de retorno. '''
    
    contador = 0
    suma_retorno = 0
    lista_cast = list() 
    sub_lista_dic = dict() 
   
    for i in range(len(df_c)): #Recorremos el dataset credits
       
            lista_cast = df_c.iloc[i]['cast']
            lines = [line.strip() for line in lista_cast.split('\n') if line.strip() != ''] 
            xy = ast.literal_eval(str(lines[0].split('"')).strip("[]").strip("'"))
            removed_chars = ['[', ']']
 
            chars = set(removed_chars)
            res = ''.join(filter(lambda x: x not in chars, xy))
            
            for elem in res:      #se accede  a cada elemento de la lista (en este caso cada elemento es un dictionario)
            
               
                for k,v in sub_lista_dic.items(): #se accede a cada llave(k), valor(v) de cada diccionario
                    if nombre_actor.lower == v.lower():
                        print("se hallo", k, v)
                
                        
                      
    return 0  
"""
print(Leer_score_titulo("Sabrina"))

print(Leer_votos_titulo("Toy Story")[0])

Leer_get_actor('Juliette Binoche')
 # pruebas...

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