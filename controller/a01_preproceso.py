
import os, sys
sys.path.append(os.getcwd())
# Lee los datos de ventas
import pandas as pd 

df_itens_pedidos = pd.read_csv("base/itens_pedidos.csv", sep = ",")

df_pedidos = pd.read_csv("base/pedidos.csv", sep = ",")

df_productos = pd.read_csv("base/productos.csv", sep = ",")

df_vendedores = pd.read_csv("base/vendedores.csv", sep = ",")



# Módulo para almacenar las variables calculadas
class DataStorage:
    df_itens_pedidos = None
    df_pedidos = None
    df_productos = None
    df_vendedores = None
    
# Eliminando columnas no necesarias, nuestro tabla de hechos, es decir
# la central será itens_pedidos
columnas_redundantes_pedidos = ["producto_id","vendedor_id"]
df_pedidos = df_pedidos.drop(columnas_redundantes_pedidos, axis = True)

# Eliminando del data frame productos sku, esta columna hace
# referencia a un código que permite identificar en almacén
# el producto, es un identificador unico del producto.

df_productos = df_productos.drop("sku", axis = True)


# Tratando los datos nulos

def eliminando_nulos(df):
    nulos = df.isnull().sum().sum()
    if nulos > 0:
        df = df.dropna().reset_index()
    else:
        df = df
    return df
   
# Eliminando nulos de df_itens_pedidos
df_itens_pedidos = eliminando_nulos(df_itens_pedidos)

# Eliminando nulos de df_pedidos
df_pedidos = eliminando_nulos(df_pedidos)

# Eliminando nulos de df_productos
df_productos = eliminando_nulos(df_productos)

# Eliminando nulos de df_vendedores
df_vendedores = eliminando_nulos(df_vendedores)



#  Eliminand los datos duplicados

def eliminando_duplicados(df):
    nulos = df.duplicated().sum()
    if nulos > 0:
        df = df.drop_duplicates().reset_index()
    else:
        df = df
    return df
   
# Eliminando nulos de df_itens_pedidos
df_itens_pedidos = eliminando_duplicados(df_itens_pedidos)

# Eliminando nulos de df_pedidos
df_pedidos = eliminando_duplicados(df_pedidos)

# Eliminando nulos de df_productos
df_productos = eliminando_duplicados(df_productos)

# Eliminando nulos de df_vendedores
df_vendedores = eliminando_duplicados(df_vendedores)



# Valores Unicos
columnas_itens = df_itens_pedidos.columns
for columna in columnas_itens:
    print(columna, df_itens_pedidos[columna].unique())
    print("#----------------------------------------#")
    

columnas_pedidos = df_pedidos.columns
for columna in columnas_pedidos:
    print(columna, df_pedidos[columna].unique())
    print("#----------------------------------------#")


columnas_producto = df_productos.columns
for columna in columnas_producto:
    print(columna, df_productos[columna].unique())
    print("#----------------------------------------#")


columnas_vendedores = df_vendedores.columns
for columna in columnas_vendedores:
    print(columna, df_vendedores[columna].unique())
    print("#----------------------------------------#")

# Seleccionando los registros con vendedores conocidos, los que marcan Unknown serán descartadas
df_vendedores = df_vendedores[df_vendedores['nombre_vendedor'] != 'Unknown']
print(df_vendedores["nombre_vendedor"].unique())

print(df_vendedores.info())

DataStorage.df_itens_pedidos=(df_itens_pedidos)
df_itens_pedidos=df_itens_pedidos.copy()

DataStorage.df_pedidos=(df_pedidos)
df_pedidos=df_pedidos.copy()

DataStorage.df_productos=(df_productos)
df_productos=df_productos.copy()

DataStorage.df_productos=(df_productos)
df_productos=df_productos.copy()