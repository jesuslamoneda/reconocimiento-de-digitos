from shutil import rmtree
import os
import matplotlib.pyplot as plt 

def generar_imagenes(test, num_generar_imagenes):

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
        plt.set_cmap(cmap='gray')
        plt.imshow(fig.reshape(28, 28))
        #plt.imshow(fig.reshape(28,28), cmap='gray')
        plt.savefig(ruta)
        plt.close()
        i = i + 1
        if (i == num_generar_imagenes):
            break