from sklearn.linear_model import LogisticRegression
from leer_csv import cargar_datos
import numpy as np
from PCA import pca_transformacion

def ejecutar_algoritmo(labels, train, test, valor_pca):
    
    #labels, train, test = cargar_datos(path_train, path_test)

    matriz_train = np.mat(train)
    num_componentes = valor_pca

    train_pca, test_pca = pca_transformacion(num_componentes=num_componentes, matriz_train=matriz_train, test=test)

    print ("Ajustamos el algoritmo de Regresion Logística")
    logreg = LogisticRegression(solver='lbfgs')
    logreg.fit(train_pca, labels)

    precision = logreg.score(train_pca, labels)

    print ("Prediciendo los datos...")
    prediccion = logreg.predict(test_pca)

    print("Precisión con el algoritmo de Regresion Logística: {:.4f}".format(precision))

    return (test, prediccion, precision)