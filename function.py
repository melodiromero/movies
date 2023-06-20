import pandas as pd
import numpy as np
import datetime as dt

# Importamos el dataset de trabajo
df = pd.read_csv('./dataset/dataset_limpio.csv', delimiter=',')

def Leer_cantidad_filmaciones_mes(mes):
    
