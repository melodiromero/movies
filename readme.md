# <h1 align=center> ** MOVIES ** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

Este es un proyecto de ingenieria de datos y de manchine learning. Como dataset se tiene una fuente de datos de peliculas a la cual se le aplica un proceso de ETL seguido del desarrollo de una API que permite realizar consultas a la misma, para finalizar con un modelo de recomendación de peliculas.

Espero sirva al lector y cualquier crítica pueden contactarme por email a: melodimarisel@gmail.com

<hr>  

## Contenido
1. [Fuente de datos](#fuente-datos)
2. [Tecnologías utilizadas](#tecnologias)
3. [ETL: limpieza, transformación y carga de datos ](#etl)
4. [Endpoint de la api ](#etl)
5. [Deploy de la api ](#etl)

## 1. Fuente de datos
***
+ [Dataset](/dataset): 2 archivos con datos que requieren ser procesados (movies_dataset.csv y credits.csv). 
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.

## 2. Technologías utilizadas
***
+ Python: para limpieza y transformación de datos, se utilizan jupyter notebook y las librerias de pandas, numpy, json. 
+ Fastapi e uvicorn: para la realización de la api. 
+ Visual Studio Code: para el desarrollo del código del proyecto. 
+ GitHub : como repositorio del proyecto
+ Render : para desployar la api.


## 3. ETL: limpieza, transformación y carga de datos
***
Se realizó lo siguiente

+ Eliminación de campos no necesarios: se eliminaron los campos que no se utilizarán en la api **video**,**imdb_id**, **adult** ,**original_title**, **poster_path** y **homepage**. 

+ Se deshanidaron las columnas **belongs_to_collection**, **production_companies**, **production_countries** para ser utilizadas más adelante en métodos de la api.

+ Eliminación de registros duplicados. 

+ Se imputaron con el valor 0 en las columnas de renueve y budget que estaban nulos o vacios. Asimismo para budget como debe ser un campo numerico tipo float, se imputaron en 0 aquellos registros que tenian en su columna datos tipo texto. Se pasan renueve y budget a tipo de dato float.

+ Para el campo release_date (fecha de estreno) se imputadon valores numericos 1, 12 y 22 por None, porque no corresponden al tipo de dato fecha y segundo, para luego eliminarlos. En el siguiente paso se eliminaron los vacios o nulos pues no servian los registros nulos para las posteriores consultas en la api. Finalmente release_date pasa a ser tipo date y tener el formato AAAA-mm-dd, además se calculó la columna ***release_year**.

+ Se adicionó la columna **retorno** que es la diferencia de **revenue y budget, campo necesario para la consulta en los endpoints de la api.

<br/>

## 4. Endpoint de la api
***
Las consultas de las api son las siguientes
  
+ def **peliculas_idioma( *`Idioma: str`* )**:
    Se ingresa un idioma y retorna la cantidad de películas producidas en ese idioma.

+ def **peliculas_duracion( *`Pelicula: str`* )**:
    Se ingresa una pelicula y retorna la duración y el año.
   
+ def **franquicia( *`Franquicia: str`* )**:
    Se ingresa la franquicia y retorna la cantidad de peliculas, ganancia total y promedio.

+ def **peliculas_pais( *`Pais: str`* )**:
    Se ingresa un país y se retorna la cantidad de peliculas producidas en el mismo.

+ def **productoras_exitosas( *`Productora: str`* )**:
    Se ingresa la productora y retorna el revunue total y la cantidad de peliculas que realizó.

+ def **get_director( *`Director: str`* )**:
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, retorna el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

<br/>

## 5. Deploy de la api
