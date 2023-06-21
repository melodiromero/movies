from fastapi import FastAPI  # importamos FastAPI necesario para la api
import function as f

app = FastAPI()  # Creacion de la api

@app.get("/")
def index():  # Funcion principal
    return {"message" :"Hola!"}

@app.get("/leer_cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(Mes:str): 
    """ Se ingresa un mes en idioma Español. 
    Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
    Ejemplo de retorno: X cantidad de películas fueron estrenadas en el mes de X
    """ 
    return {"message" :f.Leer_cantidad_filmaciones_mes(Mes)}
