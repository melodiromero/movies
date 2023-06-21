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
        raise HTTPException(status_code=404, detail="{mes} no es un mes válido. ")

@app.get('/cantidad_filmaciones_dia{dia}')
def cantidad_filmaciones_dia(dia:str):
    ''' Se ingresa el dia en idioma Español y la función retorna la cantidad de peliculas que se estrebaron ese dia historicamente. '''
    return {'dia':dia, 'cantidad':8}
