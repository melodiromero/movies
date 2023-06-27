from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
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
        return {'mes':{mes}, 'cantidad':cantidad} 
    else:
        raise HTTPException(status_code=400, message="Ocurrio una excepción, mes valido pero la salida es 0. ") 

@app.get('/cantidad_filmaciones_dia{dia}')
def cantidad_filmaciones_dia(dia:str):
    ''' Se ingresa el dia en idioma Español y la función retorna la cantidad de peliculas que se estrebaron ese dia historicamente. '''
    if f.ValidarDia(dia) == 0:
        return JSONResponse(
        status_code=400,
        content={"message": "El dato ingresado no es un dia válido."},
        )

    cantidad = f.Leer_cantidad_filmaciones_dia(dia)
    if  cantidad > 0:
        return {'mes':{dia}, 'cantidad':cantidad} 
    else:
        raise HTTPException(status_code=400, message="El dato ingresado no es un mes válido. ")

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score. '''
    datos = f.Leer_score_titulo(titulo)
    return {"mensagge": datos}

"""
    if datos == 0:
        return JSONResponse(
        status_code=404,
        content={"message": "No hay resultados con el título de la película ingresado. "},
        )
        #raise HTTPException(status_code=404, message="No hay resultados con el título de la película ingresado. ")
    else:"""
    
@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos 
    y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, 
    no se devuelve ningun valor.'''
    datos = f.Leer_votos_titulo(titulo)
    return datos