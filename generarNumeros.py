#IMPORTACION DE LIBRERIAS
import generacionNumerosAleatorios

#USO DE LA LIBRERIA
def validarCantidad(cant):
    if not isinstance(cant, int):
        raise ValueError("La cantidad debe ser un número entero.")
    if cant <= 0:
        raise ValueError("La cantidad no puede ser menor a 1.")

def generarNumerosUniforme(a, b, cant):
    validarCantidad(cant)
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroUniforme(a, b)
        x.append(v)
    return x

def generarNumerosExponencial(param, cant):
    validarCantidad(cant)
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroExponencial(param)
        x.append(v)
    return x

def generarNumerosNormalBoxMuller(media, des, cant):
    validarCantidad(cant)
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numerosNormalBoxMuller(media, des)
        x.append(v)
    return x

def generarNumerosNormalConvolucion(media, des, n, cant):
    validarCantidad(cant)
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroNormalConvolucion(media, des, n)
        x.append(v)
    return x

def generarNumerosPoisson(lambd, cant):
    validarCantidad(cant)
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroPoisson(lambd)
        x.append(v)
    return x

def generarNumerosCongruencialLineal(seed, k, c, g, cant):
    validarCantidad(cant)
    x = []
    for _ in range(cant):
        v = generacionNumerosAleatorios.numeroCongruenciaLineal(seed, k, c, g)
        x.append(v)
    return x
