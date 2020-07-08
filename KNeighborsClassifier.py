from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from leer_csv import cargar_datos #importamos la funcion en la que obteniamos los datos
from PCA import pca_transformacion

def ejecutar_algoritmo(labels, train, test, valor_pca):
    
    #labels, train, test = cargar_datos(path_train, path_test)

    #con la función cargar_datos, el train que hemos obtenido es un conjunto de arrays formados por cada una de las filas de nuestro csv
    #ahora, convertimos el set de entrenamiento en una matriz, para convertir cada array del train en distintas filas de la matriz
    matriz_train = np.mat(train)

    # a continuación vamos a usar PCA para reducir dimensiones (Principal Component Analysis)
    num_componentes = valor_pca

    #pca_transformacion(num_componentes, matriz_train, test)
    train_pca, test_pca = pca_transformacion(num_componentes=num_componentes, matriz_train=matriz_train, test=test)

    print ("Ajustamos el algoritmo k-nearest neighbors con k=10, kd_tree")
    knn = KNeighborsClassifier(n_neighbors=10, algorithm="kd_tree")
    knn.fit(train_pca, labels)

    precision = knn.score(train_pca, labels)

    print ("Prediciendo los datos...")
    prediccion = knn.predict(test_pca)

    print("Precision con el algoritmo k-nearest Neighbors: {:.4f}".format(precision))
    '''
    if (precision>=0.95):
        print("Se han predecido los datos con alta precisión")
    else:
        print("La predicción de los datos no ha sido muy buena")
    '''

    return (test, prediccion, precision)
