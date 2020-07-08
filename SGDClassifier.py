from sklearn.linear_model import SGDClassifier
from leer_csv import cargar_datos
import numpy as np
from PCA import pca_transformacion

def ejecutar_algoritmo(labels, train, test, valor_pca):
    #labels, train, test = cargar_datos(path_train, path_test)

    matriz_train = np.mat(train)
    num_componentes = valor_pca

    train_pca, test_pca = pca_transformacion(num_componentes=num_componentes, matriz_train=matriz_train, test=test)

    print ("Ajustamos el algoritmo SGD Classifier")
    sgd = SGDClassifier()
    sgd.fit(train_pca, labels)

    precision = sgd.score(train_pca, labels)

    print ("Prediciendo los datos...")
    prediccion = sgd.predict(test_pca)

    print("Precisión con el algoritmo SGD Classifier: {:.4f}".format(precision))

    return (test, prediccion, precision)