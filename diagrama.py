import seaborn as sns
import matplotlib as mpl
mpl.use('Agg') #para solucionar un error con matplotlib que se da en flask

def generar_diagrama(datos, nombre, label):

    ruta = "static/imagenes/diagramas/" + nombre

    diagrama = sns.countplot(datos)
    diagrama.set_xlabel(label)
    diagrama.figure.savefig(ruta)
    
    mpl.importlib.reload(mpl); mpl.importlib.reload(mpl.pyplot); mpl.importlib.reload(sns) #para reiniciar los valores de seaborn y matplotlib, sino se me guardan dos diagramas iguales

    print("Diagrama con la distribución de los dígitos %s generado" % nombre)