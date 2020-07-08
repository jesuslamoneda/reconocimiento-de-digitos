#fichero para cargar los datos

import csv
import numpy as np
#import seaborn as sns
#import matplotlib
#matplotlib.use('Agg')

def cargar_datos(path_train, path_test):
    print("Leyendo datasets")
    csv_train = csv.reader(open(path_train, "r"), delimiter=",") #abrimos el fichero de entrenamiento csv en modo lectura

    #para entrenar el modelo, vamos a separar los datos de la solucion (label)
    train = []
    labels = []

    print("Procesando conjunto de entrenamiento")

    i=0
    for row in csv_train: #recorremos fila por fila de todo el dataset

        if (i!=0): #no trabajamos con la primera fila, ya que son los headers
            labels.append(int(row[0])) #la primera columna de cada fila corresponde al resultado, el digito resultante, por ello lo guardamos en otro array
            row = row[1:] #ya hemos obtenido el valor de la label de la fila, por lo que nos quedamos con el resto (del elemento 1 en adelante, el 0 era la label), que serán nuestros datos

            train.append(np.array(np.int64(row))) #insertamos nuestra fila de datos (sin la label)
        i=i+1

    csv_test = csv.reader(open(path_test, "r"), delimiter=",")

    print("Procesando conjunto de tests")
    test = []
    i=0
    for row in csv_test:

        if (i!=0):
            test.append(np.array(np.int64(row)))
        #en el dataset de Test no tenemos contenidas las soluciones, ya que es en el que haremos nuestra predicción después de entrenar el modelo, y por ello no tenemos que separar la columna label
        i=i+1

    #diagrama = sns.countplot(labels)
    #diagrama.figure.savefig("static/imagenes/diagramas/train.png")
    #print("Diagrama con la distribución de los dígitos en el conjunto de entrenamiento generado")
    return (labels, train, test)

if __name__ == '__main__':
    labels, train, test = cargar_datos("/Users/jesuslamoneda/Downloads/recognizer-website/src/datasets/train.csv", "/Users/jesuslamoneda/Downloads/recognizer-website/src/datasets/test.csv")
    