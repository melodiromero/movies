# <h1 align=center> ** MOVIES ** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

Este es un proyecto de ingenieria de datos y de manchine learning. Como dataset se tiene una fuente de datos de peliculas a la cual se le aplica un proceso de ETL seguido del desarrollo de una API que permite realizar consultas a la misma, para finalizar con un modelo de recomendación de peliculas.

Espero sirva al lector y cualquier crítica pueden contactarme por email a: melodimarisel@gmail.com

<hr>  

## Contenido
1. [Fuente de datos](#fuente-datos)
2. [Tecnologías utilizadas](#tecnologias)
3. [ETL: limpieza, transformación y carga de datos ](#etl)
4. [Endpoint Api ](#etl)

### Fuente de datos
***
+ [Dataset](/dataset): 2 archivos con datos que requieren ser procesados (movies_dataset.csv y credits.csv). 
+ [Diccionario de datos](agregar): Diccionario con algunas descripciones de las columnas disponibles en el dataset.

## Technologías utilizadas
***
+ Python: para limpieza y transformación de datos, se utilizan jupyter notebook y las librerias de pandas, datetime. 
+ Fastapi e uvicorn: para la realización de la api. 
+ Visual Studio Code: para el desarrollo del código del proyecto. 


## ETL: limpieza, transformación y carga de datos
***
Se realizó lo siguiente

+ Eliminación de campos no necesarios: se eliminaron los campos que no se utilizarán en la api **video**,**imdb_id**, **adult** ,**original_title**, **poster_path** y **homepage**. 

+ Eliminación de registros duplicados. 

+ Se imputaron con el valor 0 en las columnas de renueve y budget que estaban nulos o vacios. Asimismo para budget como debe ser un campo numerico tipo float, se imputaron en 0 aquellos registros que tenian en su columna datos tipo texto. Se pasan renueve y budget a tipo de dato float.

+ Para el campo release_date (fecha de estreno) se imputadon valores numericos 1, 12 y 22 por None, porque no corresponden al tipo de dato fecha y segundo, para luego eliminarlos. En el siguiente paso se eliminaron los vacios o nulos pues no servian los registros nulos para las posteriores consultas en la api. Finalmente release_date pasa a ser tipo date y tener el formato AAAA-mm-dd, además se calcularon las columnas ***release_year**, **release_month** y **release_day_of_week** para ser utilizadas en los metodos de la api.

+ Se adicionó la columna **retorno** que es la diferencia de **revenue y budget, campo necesario para la consulta en los endpoints de la api.

<br/>

## Endpoint de la api
***
Las consultas de las api son las siguientes
  
+ def **cantidad_filmaciones_mes( *`Mes`* )**:
    Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.

+ def **cantidad_filmaciones_dia( *`Dia`* )**:
    Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.

+ def **score_titulo( *`titulo_de_la_filmación`* )**:
    Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.

+ def **votos_titulo( *`titulo_de_la_filmación`* )**:
    Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
 
+ def **get_actor( *`nombre_actor`* )**:
    Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno.

+ def **get_director( *`nombre_director`* )**:
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

+ def **recomendacion( *`titulo`* )**:
    Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.

<br/>


