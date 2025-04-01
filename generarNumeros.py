#IMPORTACION DE LIBRERIAS
import generacionNumerosAleatorios
#USO DE LA LIBRERIA
def generarNumerosUniforme(a,b,cant):
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroUniforme(a,b)
        x.append(v)
    return x
def generarNumerosExponencial(param,cant):
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroExponencial(param)
        x.append(v)
    return x
def generarNumerosNormalBoxMuller(media,des,cant):
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numerosNormalBoxMuller(media,des)
        x.append(v)
    return x
def generarNumerosNormalConvolucion(media,des,n,cant):
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroNormalConvolucion(media,des,n)
        x.append(v)
    return x
def generarNumerosPoisson(lambd,cant):
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroPoisson(lambd)
        x.append(v)
    return x
def generarNumerosCongruencialLineal(seed,k,c,g,cant):
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroCongruenciaLineal(seed,k,c,g)
        x.append(v)
    return x

