# <h1 align=center> ** MOVIES ** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

Este es un proyecto de ingeniería de datos y de manchine learning. Como dataset se tiene una fuente de datos de peliculas a la cual se le aplica un proceso de ETL (Extracción, Transformación y Carga) seguido de un EDA (Análisis Exploratorio de Datos) y a posteriori, el desarrollo de una API (Interfaz de Programación de Aplicaciones) que permite realizar consultas a la misma, para finalizar con un modelo de recomendación de peliculas que forma parte de uno de los endpoints de la API.

Espero sirva al lector y cualquier sugerencia o crítica pueden contactarme por email a: melodimarisel@gmail.com

<hr>  

## Contenido
1. [Fuente de datos](#fuente-datos)
2. [Tecnologías utilizadas](#tecnologias)
3. [ETL: limpieza, transformación y carga de datos ](#etl)
4. [EDA: análisis exploratorio de datos ](#eda)
5. [Sistemas de recomendación ](#ml)
6. [Endpoint de la api ](#api)
7. [Deploy de la api ](#conclusion)

## 1. Fuente de datos
***
+ [Dataset](/dataset): 2 archivos con datos que requieren ser procesados (movies_dataset.csv y credits.csv). 
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.

## 2. Technologías utilizadas
***
+ Python: para limpieza y transformación de datos, se utilizan jupyter notebook y las librerias de pandas, numpy, matplotlib, seaborn, wordcloud, sklearn, fastapi y uvicorn
+ Fastapi e uvicorn: para la realización de la api. 
+ Visual Studio Code: para el desarrollo del código del proyecto. 
+ GitHub : como repositorio del proyecto
+ Render : para desployar la api.


## 3. ETL: limpieza, transformación y carga de datos
***
Se realizó un análisis de la fuente de datos y preparación de los datos para su posterior análisis y visualización, para lo cual se realizaron las siguientes transformaciones:

+ Eliminación de campos no necesarios: se eliminaron los campos que no se utilizarán en la api **video**,**imdb_id**, **adult** ,**original_title**, **poster_path** y **homepage**. 

+ Se deshanidaron las columnas **belongs_to_collection**, **production_companies**, **production_countries** para ser utilizadas más adelante en métodos de la api.

+ Eliminación de registros duplicados. 

+ Se imputaron con el valor 0 en las columnas de renueve y budget que estaban nulos o vacios. Asimismo para budget como debe ser un campo numerico tipo float, se imputaron en 0 aquellos registros que tenian en su columna datos tipo texto. Se pasan renueve y budget a tipo de dato float.

+ Para el campo release_date (fecha de estreno) se imputadon valores numericos 1, 12 y 22 por None, porque no corresponden al tipo de dato fecha y segundo, para luego eliminarlos. En el siguiente paso se eliminaron los vacios o nulos pues no servian los registros nulos para las posteriores consultas en la api. Finalmente release_date pasa a ser tipo date y tener el formato AAAA-mm-dd, además se calculó la columna ***release_year**.

+ Se adicionó la columna **retorno** que es la diferencia de **revenue y budget, campo necesario para la consulta en los endpoints de la api.

<br/>

## 4. EDA: análisis exploratorio de datos
***
Se exploran los datos para comprender su estructura, patrones, relaciones y características. 
En este proceso se obtienen los registros atípicos (outliers), se buscan patrones y relaciones en el dataset objeto de estudio.

+ En la visualización de la estadistica descriptiva de los datos, se observan que las peliculas registras datan de los años 1874 al 2020. Entre ellas hay filmaciones con presupuesto y ganancia en cero. También se observa que hay peliculas que no tienen valoración registrada (sus registros están en cero), en cuanto a puntuación por polularidad TMDB (TheMoviesDataBase), reseña y votación.

+ Para la detección de valores atípicos se utilizó el método de de Tukey's fences.

+ Entre los campos "budget" y "revenue" se aprecia una correlación positiva fuerte entre estas dos variables. Se puede afirmar que cuando el presupuesto (budget) de una película aumenta, también aumenta los ingresos (revenue) generados por esa película.

+ Las cinco palabras más frecuentes analizando el titulo de las filmaciones son: Love, Man, Girl, Nigth y Day. Cuando se analiza el resumen de la pelicula las más frecuente son: Life, Find, Love, One y(live, film y family parecieran estan en el 5to orden al mismo nivel).

## 5. Sistema de recomendación




## 6. Endpoint de la api
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

## 7. Deploy de la api
La api se encuentra disponible en la siguiente dirección:
https://sistema-recomendacion-peliculas-2aos.onrender.com

Y su documentación con la posibilidad de interactual con los endpoints
https://sistema-recomendacion-peliculas-2aos.onrender.com/docs