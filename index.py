from flask import Flask, render_template, request, send_from_directory
from pathlib import Path

app = Flask(__name__)

path_datasets = "static/datasets"
path_datasets_train = "static/datasets/train"
path_datasets_test = "static/datasets/test"
#num_imagenes = 30
pca_send = 0
prediccion = []
train_send = ""
test_send = ""
precision = 0
algoritmo_usado = ""
num_imagenes = 0
num_algoritmo = -1

#Jesús La Moneda Cué 8/07/2020

@app.route('/', methods=['GET', 'POST'])  # esta va a ser la ruta principal
def home():
    global path_datasets
    global path_datasets_train
    global path_datasets_test
    global pca_send
    global prediccion
    global train_send
    global test_send 
    global precision 
    global algoritmo_usado
    global num_algoritmo
    global num_imagenes

    if request.method == 'GET':
        if (len(prediccion)): #si ya hemos cargado estos datos previamente, se mostrarán
            return render_template('inicio.html', seleccionado_digito=False, num_algoritmo=num_algoritmo, pca=pca_send, train_send=train_send, test_send=test_send, procesado=True, precision=precision, algoritmo_usado=algoritmo_usado, num_imagenes=num_imagenes, prediccion=prediccion)

        archivos_train = listar_archivos(path=path_datasets_train)
        archivos_test = listar_archivos(path=path_datasets_test)
        return render_template('inicio.html', procesado=False, pca=16, archivos_train=archivos_train, archivos_test=archivos_test, cargando=False, num_imagenes = 25)

    if request.method == 'POST':

        if (request.form.get("procesar")):
            print("Se ha pulsado procesar")

            algoritmo_send = int(request.form.get("algoritmo"))
            pca_send = int(request.form.get("pca_form"))
            train_send = request.form.get("train_form")
            test_send = request.form.get("test_form")
            num_imagenes_send = request.form.get("num_imagenes_form")
            num_imagenes = int(num_imagenes_send)

            from predecir import generar
            #path_train = path_datasets + '/' + train_send
            #path_test = path_datasets + '/' + test_send
            path_train = path_datasets_train + '/' + train_send
            path_test = path_datasets_test + '/' + test_send
            prediccion, precision = generar(
            algoritmo_send, path_train, path_test, pca_send, num_generar_imagenes=num_imagenes)

            if (int(algoritmo_send) == 1):
                algoritmo_usado = "Decision Tree Classifier"
            elif (int(algoritmo_send) == 2):
                algoritmo_usado = "KNeighbors Classifier"
            elif (int(algoritmo_send) == 3):
                algoritmo_usado = "Logistic Regression"
            elif (int(algoritmo_send) == 4):
                algoritmo_usado = "Random Forest Classifier"
            elif (int(algoritmo_send) == 5):
                algoritmo_usado = "Ridge Classifier"
            elif (int(algoritmo_send) == 6):
                algoritmo_usado = "SGD Classifier"
            else:
                algoritmo_usado = "Support Vector Machine"

            precision = precision*100
            num_algoritmo = int(algoritmo_send)
        
            return render_template('inicio.html', seleccionado_digito=False, num_algoritmo=num_algoritmo, pca=pca_send, train_send=train_send, test_send=test_send, procesado=True, precision=precision, algoritmo_usado=algoritmo_usado, num_imagenes=num_imagenes, prediccion=prediccion)

        elif (request.form.get("vista")) :
        #else:
            print("Se ha pulsado vista")

            digito_send = int(request.form.get("digito_form"))
            lista_digitos = []
            
            if (digito_send==-1): #mostrar todos
                return render_template('inicio.html', seleccionado_digito=False, num_algoritmo=num_algoritmo, pca=pca_send, train_send=train_send, test_send=test_send, procesado=True, precision=precision, algoritmo_usado=algoritmo_usado, num_imagenes=num_imagenes, prediccion=prediccion)
            
            else: #mostrar digito concreto

                for i in range(0, num_imagenes):
                    if (int(prediccion[i])==int(digito_send)):
                        lista_digitos.append(i)
            
                print(lista_digitos)

                return render_template('inicio.html', seleccionado_digito=True, num_algoritmo=num_algoritmo, digito_escogido=digito_send, pca=pca_send, train_send=train_send, test_send=test_send, procesado=True, precision=precision, num_imagenes=num_imagenes, algoritmo_usado=algoritmo_usado, lista_digitos=lista_digitos, tam_lista=len(lista_digitos))

        else:
            print("Se ha pulsado reset")
            pca_send = 0
            prediccion = []
            train_send = ""
            test_send = ""
            precision = 0
            algoritmo_usado = ""
            num_imagenes = 0
            num_algoritmo = -1

            archivos_train = listar_archivos(path=path_datasets_train)
            archivos_test = listar_archivos(path=path_datasets_test)
            return render_template('inicio.html', procesado=False, pca=16, archivos_train=archivos_train, archivos_test=archivos_test, cargando=False, num_imagenes = 25)

        
@app.route('/info')
def about():
    return render_template('informacion.html')

'''
@app.route('/upload', methods=['GET', 'POST'])
def subir():
    if request.method == 'GET':
        return render_template('predecir_imagen.html')

    if request.method == 'POST':
        print(request.files)
        if 'imagen_subida' not in request.files:
            print('No se ha subido ninguna imagen')

        file = request.files['imagen_subida']
        imagen = file.read()
        print(imagen)
        resultado = 0

        return render_template('predecir_imagen.html', prediccion=resultado)
'''

@app.route('/descargas/<path:nombre_archivo>', methods=['GET', 'POST'])
def download(nombre_archivo):
    ruta = "static/descargas"
    print(nombre_archivo)
    
    return send_from_directory(directory=ruta, filename=nombre_archivo)


def listar_archivos(path):
    return [obj.name for obj in Path(path).iterdir() if obj.is_file()]


if __name__ == '__main__':  # así sabemos que estamos ejecutando la clase y no  está siendo importada
    app.run(debug=True)
