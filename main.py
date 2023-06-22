from fastapi import FastAPI, HTTPException  # importamos FastAPI necesario para la api
import function as f

app = FastAPI()  # Creacion de la api

@app.get("/")
def index():  # Funcion principal
    return {"message" :"Hola!"}

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes:str): 
    ''' Se ingresa un mes en idioma Español y la función retorna la cantidad de peliculas que se estrenaron ese mes historicamente. '''
    
    cantidad = f.Leer_cantidad_filmaciones_mes(mes)
    if  cantidad > 0:
        return {'mes':{mes}, 'cantidad':cantidad} 
    else:
        raise HTTPException(status_code=400, message="El dato ingresado no es un mes válido. ")

@app.get('/cantidad_filmaciones_dia{dia}')
def cantidad_filmaciones_dia(dia:str):
    ''' Se ingresa el dia en idioma Español y la función retorna la cantidad de peliculas que se estrebaron ese dia historicamente. '''
    cantidad = f.Leer_cantidad_filmaciones_dia(dia)
    if  cantidad > 0:
        return {'mes':{dia}, 'cantidad':cantidad} 
    else:
        raise HTTPException(status_code=400, message="El dato ingresado no es un mes válido. ")

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score. '''
    datos = f.Leer_score_titulo(titulo)

    if datos == 0:
        raise HTTPException(status_code=404, message="No hay resultados con el título de la película ingresado. ")
    else:
        return datos