from sklearn.svm import SVC
from leer_csv import cargar_datos #importamos la funcion en la que obteniamos los datos
import numpy as np
from PCA import pca_transformacion

def ejecutar_algoritmo(labels, train, test, valor_pca):
    #labels, train, test = cargar_datos(path_train, path_test)

    matriz_train = np.mat(train)
    num_componentes = valor_pca

    train_pca, test_pca = pca_transformacion(num_componentes=num_componentes, matriz_train=matriz_train, test=test)

    print ("Ajustamos el algoritmo SVC")
    #svc = SVC(gamma='auto')
    svc = SVC()
    svc.fit(train_pca, labels)

    precision = svc.score(train_pca, labels)

    print ("Prediciendo los datos...")
    prediccion = svc.predict(test_pca)

    print("Precisión con el algoritmo Support Vector Classifier: {:.4f}".format(precision))

    return (test, prediccion, precision)
