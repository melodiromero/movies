# Se importan las librerias a utilizar
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from memory_profiler import profile

df  = pd.read_csv('./dataset/movies_reducido.csv', delimiter=',')

# Se eliminan los registros duplicados
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

#se imputan los nulos o nan con ''
titulo = df['title'].fillna('')

tfidf = TfidfVectorizer(stop_words='english', lowercase=True) # configuracion de TfidfVectorizery, en idioma ingles

# se crea la una matriz TF-IDF con las puntaciones del campo title
tfidf_matrix = tfidf.fit_transform(titulo)

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix) # se calcula la matriz de coseno para los vectores.


def get_recommendations(df, column, value, cosine_similarities, limit=5):
    """ Retorna un dataframe de 5 registros recomendados según la 
        Frecuencia de término Frecuencia de documento inversa (TF-IDF) 
        y la similitud del coseno.
    
    Args:
        df (object): dataframe que contiene el texto a analizar. 
        column (string): nombre de la columna utilizada. 
        value (string): nombre del titulo a tener las recomendaciones.
        cosine_similarities (array): matriz de similitud del cosenol
        limit (int, optional): retorna la cantidad de registros a retornar recomendados. 
        
    Returns: 
        Pandas dataframe. 
    """
    
    # Return indices for the target dataframe column and drop any duplicates
    indices = pd.Series(df.index, index=df[column]).drop_duplicates()

    # Get the index for the target value
    target_index = indices[value]

    # Get the cosine similarity scores for the target value
    cosine_similarity_scores = list(enumerate(cosine_similarities[target_index]))

    # Sort the cosine similarities in order of closest similarity
    cosine_similarity_scores = sorted(cosine_similarity_scores, key=lambda x: x[1], reverse=True)

    # Return tuple of the requested closest scores excluding the target item and index
    cosine_similarity_scores = cosine_similarity_scores[1:limit+1]

    # Extract the tuple values
    index = (x[0] for x in cosine_similarity_scores)
    scores = (x[1] for x in cosine_similarity_scores)    

    # Get the indices for the closest items
    recommendation_indices = [i[0] for i in cosine_similarity_scores]

    # Get the actutal recommendations
    recommendations = df[column].iloc[recommendation_indices]

    # Return a dataframe
    df = pd.DataFrame(list(zip(index, recommendations, scores)), 
                      columns=['index','pelicula', 'cosine_similarity_score']) 

    return df

@profile
def obtenerListaPeliculas(pelicula):
    lista = get_recommendations(df, 
                                      'title', 
                                      pelicula, 
                                      cosine_similarities)
    
    
    cantidad        = len(lista)
    datos           = []
    if cantidad > 0:
        for i in range(len(lista)):
            datos.append(lista.iloc[i]['pelicula']) 

    
    return datos
    
print(obtenerListaPeliculas('Toy Story'))