from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from typing import Dict
# importamos FastAPI necesario para la api

import function as f # importamos el archivo .py que contiene los metodos que consultan el dataset.

app = FastAPI()  # Creacion de la api

@app.get("/")
def index():  # Funcion principal
    return {"message" :"Hola!"}

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes:str): 
    ''' Se ingresa un mes en idioma Español y la función retorna la cantidad de peliculas que se estrenaron ese mes historicamente. '''
    if f.ValidarMes(mes) == 0:
        return JSONResponse(
        status_code=400,
        content={"message": "El dato ingresado no es un mes válido."},
        )

    cantidad = f.Leer_cantidad_filmaciones_mes(mes)

    if  cantidad > 0:
        return {'mes':mes, 'cantidad':cantidad} 
    else:
        raise HTTPException(status_code=400, message="Ocurrio una excepción, mes valido pero la salida es 0. ") 

@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia:str):
    ''' Se ingresa el dia en idioma Español y la función retorna la cantidad de peliculas que se estrebaron ese dia historicamente. '''
    if f.ValidarDia(dia) == 0:
        return JSONResponse(
        status_code=400,
        content={"message": "El dato ingresado no es un dia válido."},
        )

    cantidad = f.Leer_cantidad_filmaciones_dia(dia)
  
    if  cantidad > 0:
        return {'dia':dia, 'cantidad':cantidad} 
    else:
        raise HTTPException(status_code=400, message="El dato ingresado no es un mes válido. ")

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score. '''
    datos = f.Leer_score_titulo(titulo)
    
    if  datos.empty == True:
        return JSONResponse(
        status_code=404,
        content={"message": "No hay resultados con el título de la película ingresado. "},
        )
        #raise HTTPException(status_code=404, message="No hay resultados con el título de la película ingresado. ")
    else:
       
        jsoned = datos
        return {"message": jsoned}
    """
        # Convertir el diccionario a JSON serializable
        json_resultado = jsonable_encoder(datos)

        # Crear una instancia de Response con el contenido JSON
        response = Response(content=json_resultado, media_type="application/json")

        # Devolver la instancia de Response
        return response
"""

@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo:str):
    ''' Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos 
        y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, 
        caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, 
        no se devuelve ningun valor. '''
    datos = ''
    datos = f.Leer_votos_titulo(titulo)
    
    #print(datos)
    # Convertir el diccionario a JSON serializable
    json_resultado = jsonable_encoder(datos)

    # Crear una instancia de Response con el contenido JSON
    response = Response(content=json_resultado, media_type="application/json")

    # Devolver la instancia de Response
    return response

    """
    if datos == 1:
            return JSONResponse(
            status_code=202,
            content={"message": "La filmación no cumple con la condición de al menos 2000 valoraciones. "},
            )
            #raise HTTPException(status_code=404, message="No hay resultados con el título de la película ingresado. ")
    else:
            if datos == 0:
                return JSONResponse(
                status_code=404,
                content={"message": "No existe una filmación con el titulo de película ingresado. "},
                )
            #raise HTTPException(status_code=404, message="No hay resultados con el título de la película ingresado. ")
            else:          
               
                # Convertir el diccionario a JSON serializable
                json_resultado = jsonable_encoder(datos)

                # Crear una instancia de Response con el contenido JSON
                response = Response(content=json_resultado, media_type="application/json")

                # Devolver la instancia de Response
                return response
                
"""
"""

@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor:str):
    ''' Se ingresa el nombre de un actor que se encuentre dentro del dataset debiendo devolver
        el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en 
        las que ha participado y el promedio de retorno. '''
    
    return {'actor':nombre_actor, 'cantidad_filmaciones':respuesta, 'retorno_total':respuesta, 'retorno_promedio':respuesta}

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.'''
    return {'director':nombre_director, 'retorno_total_director':respuesta, 
    'peliculas':respuesta, 'anio':respuesta,, 'retorno_pelicula':respuesta, 
    'budget_pelicula':respuesta, 'revenue_pelicula':respuesta}

# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    return {'lista recomendada': respuesta}
    
"""