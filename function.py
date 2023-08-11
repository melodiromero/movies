import pandas as pd
# Se importa el dataset de trabajo
df  = pd.read_csv('./dataset/movies_limpio.csv', delimiter=',')
# Declaración de estructuras de datos necesarios para los metodos.
# Diccionario de meses en español y su nro correspondiete.

idiomas = df['original_language'].unique().tolist()
# De los idiomas, se elimina los ivalidos 
if '104.0' in idiomas:
    idiomas.remove('104.0')
    
if '82.0' in idiomas:
    idiomas.remove('82.0')

if '68.0' in idiomas:
    idiomas.remove('68.0')

#print(idiomas)

def validadIdioma(idioma):
    if idioma in idiomas:
        return 1
    else:
        return 0

def leer_cantidad_peliculas_por_idioma(idioma):
    # Se retorna la cantida de peliculas registradas con el idioma ingresado.
    cantidad = len(df[df['original_language'] == idioma])
    
    return cantidad

def leer_peliculas_duracion(pelicula):
    # Se retorna la duracion y e año de la pelicula.
    subdicc = dict()
    midicc = []
    datos = df[['runtime', 'release_year']][df['title'].str.lower() == pelicula.lower()]

    for i in range(len(datos)):
        subdicc = {
                    "pelicula"  : pelicula,
                    "duracion"  : datos.iloc[i]['runtime'],
                    "anio"      : datos.iloc[i]['release_year']
                }
        midicc.append(subdicc) 
    # Se retorna como lista de diccionarios pes hay peliculas como Sabrina que tienen mas de un registro   
    return midicc  

def leer_franquicia(franquicia):
    # Se ingresa la franquicia y retorna la cantidad de peliculas, ganancia total y promedio. '''
    resultados      = df[df['franquicia'].str.lower() == franquicia.lower()]
    datos           = dict()
    cantidad        = len(resultados)
   
    if cantidad > 0:
        ganancia_total  = resultados['revenue'].sum()
        ganancia_prom   = ganancia_total / cantidad
        datos   = {
                        "franquicia"        : franquicia,
                        "cantidad"          : cantidad,
                        "ganancia_total"    : ganancia_total,
                        "ganacia_promedio"  : ganancia_prom
                }
    return datos

def leer_peliculas_pais(pais):
    # Se ingresa el pais y retorna la cantidad de peliculas producidas en el mismo. '''
    cantidad = df['paises'].str.contains(pais, case=False).sum()
    datos           = dict()
    
    if cantidad > 0:
        datos       = {
                    "pais"    : pais,
                    "cantidad": cantidad
        }
        
    return datos

def leer_productora(productora):
    # Ingresas la productora, entregandote el revenue_total total y la cantidad de peliculas que realizo. '''
    # primero, se eliminan los nulos
    resultados = df.dropna(subset=['productoras'])
    # se filtra los registros que tienen coincidencia en la columna de prooductoras
    resultados = resultados.loc[resultados['productoras'].str.contains(productora, case=False)]
   
    # se calcula la cantidad y la suma de ganancia  
    cantidad        = len(resultados)
    revenue_total   = resultados['revenue'].sum() 
    datos           = dict()
    if cantidad > 0:
        datos   = {
                        "productora"        : productora,
                        "cantidad"          : cantidad,
                        "revenue_total"     : revenue_total
                }
    return datos

