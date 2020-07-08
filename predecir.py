import matplotlib.pyplot as plt  # para la visualizacion
from shutil import rmtree
import os
from imagenes import generar_imagenes
from leer_csv import cargar_datos
from diagrama import generar_diagrama

#import KNeighborsClassifier
#import SVC
#import RandomForestClassifier
#import SGDClassifier
#import DecisionTreeClassifier
#import RidgeClassifier
#import LogisticRegression

#esta clase se encarga de entrenar el modelo con el algoritmo seleccionado, predecir los digitos del set de pruebas, generar las imagenes que se muestran, los diagramas...
def generar(num_algoritmo, path_train, path_test, valor_pca, num_generar_imagenes):
    # algoritmo = KNeighborsClassifier #eligo este

    if (num_algoritmo == 1):
        from DecisionTreeClassifier import ejecutar_algoritmo
    elif (num_algoritmo == 2):
        from KNeighborsClassifier import ejecutar_algoritmo
    elif (num_algoritmo == 3):
        from LogisticRegression import ejecutar_algoritmo
    elif (num_algoritmo == 4):
        from RandomForestClassifier import ejecutar_algoritmo
    elif (num_algoritmo == 5):
        from RidgeClassifier import ejecutar_algoritmo
    elif (num_algoritmo == 6):
        from SGDClassifier import ejecutar_algoritmo
    else:
        from SVC import ejecutar_algoritmo

    '''
    switcher = {
        1: from DecisionTreeClassifier import ejecutar_algoritmo,
        2: from KNeighborsClassifier import ejecutar_algoritmo,
        3: from LogisticRegression import ejecutar_algoritmo,
        4: from RandomForestClassifier import ejecutar_algoritmo,
        5: from RidgeClassifier import ejecutar_algoritmo,
        6: from SGDClassifier import ejecutar_algoritmo,
        7: from SVC import ejecutar_algoritmo
    }

    switcher.get(num_algoritmo, lambda: "Algoritmo no valido")
    '''

    labels, train, test = cargar_datos(path_train, path_test)
    test, prediccion, precision = ejecutar_algoritmo(labels, train, test, valor_pca)
    del train
    if os.path.isdir('static/imagenes/diagramas/'):
            # la carpeta existe, procedemos a borrarla por todo lo que pudiera contener antes
            rmtree("static/imagenes/diagramas")  # borro el directorio
            os.mkdir('static/imagenes/diagramas')  # creo de nuevo el directorio vacío
    else:
        # no existe, por lo que solo creamos el directorio
        print('La carpeta no existe, por lo que la creamos')
        os.mkdir('static/imagenes/diagramas')

    generar_diagrama(labels, "train.png", "Conjunto de entrenamiento")
    del labels
    generar_diagrama(prediccion, "test.png", "Conjunto de pruebas")

    #generar_imagenes(test, num_generar_imagenes)
    #del test

    print("Generando fichero de prediccion")
    fich_completo = "static/descargas" + '/' + "Prediccion.csv"

    import csv
    with open(fich_completo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["ID Imagen", "Resultado"])

        i=1
        for p in prediccion:
            writer.writerow([i, p])
            i = i + 1

    print("Generando Imágenes")
    if os.path.isdir('static/imagenes/digitos/'):
        # la carpeta existe, procedemos a borrarla por todo lo que pudiera contener antes
        print('La carpeta existe, por lo que la vaciamos')
        rmtree("static/imagenes/digitos")  # borro el directorio
        os.mkdir('static/imagenes/digitos')  # creo de nuevo el directorio vacío
    else:
        # no existe, por lo que solo creamos el directorio
        print('La carpeta no existe, por lo que la creamos')
        os.mkdir('static/imagenes/digitos')

    i = 0
    for image in test:  # guardamos en el directorio digitos las contenidas en el dataset test
        fig = test[i]
        ruta = 'static/imagenes/digitos/' + str(i) + '.png'

        plt.figure(figsize=[3, 3])
        plt.axis('off')
        plt.set_cmap(cmap='binary')
        plt.imshow(fig.reshape(28, 28))
        #plt.imshow(fig.reshape(28,28), cmap='gray')
        plt.savefig(ruta)
        plt.close()
        i = i + 1
        if (i == num_generar_imagenes):
            break

    return (prediccion, precision)
