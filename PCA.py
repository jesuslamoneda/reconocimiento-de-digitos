from sklearn import decomposition #va a hacer el análsis de componentes principales

def pca_transformacion(num_componentes, matriz_train, test):
    print("Ajustamos PCA para %d componentes" % num_componentes)
    pca = decomposition.PCA(n_components=num_componentes).fit(matriz_train)

    print("Reducimos la matriz de entrenaniento a los %d componentes" % num_componentes)
    X_train_reducida = pca.transform(matriz_train)

    print("Reducimos también el conjunto de test a %d componentes" % num_componentes)
    X_test_reducida = pca.transform(test)

    return (X_train_reducida, X_test_reducida)