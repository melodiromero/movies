from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
# se importa FastAPI necesario para la api

import function as f    # se importa el archivo fucntion.py que contiene los metodos que consultan el dataset.
import ml as m          # se importa el archivo ml.py que contiene el modelo de recomendacion de peliculas.

app = FastAPI()  # Creacion de la api

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='127.0.0.1')

@app.get("/")
def index():  # Funcion principal
    return {"message" :"Hola!"}

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma( idioma: str ): 
    '''Se ingresa un idioma y retorna la cantidad de películas producidas en ese idioma.'''
    if f.validadIdioma(idioma) == 0:
        return JSONResponse(
        status_code=400,
        content={"message": "El dato ingresado no es un idioma válido."},
        )
   
    cantidad = f.leer_cantidad_peliculas_por_idioma(idioma)

    if  cantidad > 0:
        return {'idioma':idioma, 'cantidad':cantidad} 
    else:
        raise HTTPException(status_code=400, message="Ocurrio una excepción, idioma vàlido pero la cantidad de peliculas es 0. ") 

@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    '''Se ingresa la pelicula y retorna la duración y el año. '''
    datos = f.leer_peliculas_duracion(pelicula)
    if len(datos) == 0:
            return JSONResponse(
            status_code=404,
            content={"message": "No existe una filmación con el titulo de película ingresado. "},
            )
    else:
        return datos

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia y retorna la cantidad de peliculas, ganancia total y promedio. '''
    datos = f.leer_franquicia(franquicia)
    if bool(datos):
        return datos
    else:
        return JSONResponse(
            status_code=404,
            content={"message": "No se hallaron datos con la franquicia ingresada. "},
            )
   
@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    '''Ingresas el pais y retorna la cantidad de peliculas producidas en el mismo. '''
    datos = f.leer_peliculas_pais(pais)
    if bool(datos):
        return datos
    else:
        return JSONResponse(
            status_code=404,
            content={"message": "No se hallaron datos con el pais ingresado. "},
        )
        
@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str):
    '''Ingresas la productora, entregandote el revunue total y la cantidad de peliculas que realizo '''
    datos = f.leer_productora(productora)
    if bool(datos):
        return datos
    else:
        return JSONResponse(
            status_code=404,
            content={"message": "No se hallaron datos con la productora ingresada. "},
        )

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. En formato lista'''
    return {'director':nombre_director, 'retorno_total_director':'', 
    'peliculas':'', 'anio':'','retorno_pelicula':'', 
    'budget_pelicula':'', 'revenue_pelicula':''}
    
# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''

    lista = m.obtenerListaPeliculas(titulo)
    if bool(lista):
        return {'lista' : lista}
    else:
        return JSONResponse(
            status_code=404,
            content={"message": "No se hallaron resultados con el titulo ingresado. "},
        )