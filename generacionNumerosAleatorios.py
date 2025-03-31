#IMPORTACION DE LIBRERIAS
import math as m
import random as r
from fractions import Fraction
#GENERACION DE VARIABLES CON DISTRIBUCION UNIFORME
def numeroUniforme(a,b,rnd=None):
    if rnd is None:
        rnd = r.random()
        if b > a:
            return a + (b - a) * rnd
        else:
            raise ValueError("El valor de b debe ser mayor que a")
    else:
        if rnd < 0 or rnd > 1:
            raise ValueError("El valor de RND debe estar entre 0 y 1")
        else: 
            if b > a:
                return a + (b - a) * rnd
            else:
                raise ValueError("El valor de b debe ser mayor que a")
#GENERACION DE VARIABLES CON DISTRIBUCION EXPONENCIAL NEGATIVA
def numeroExponencial(param, rnd=None):
    if rnd is None:
        rnd = r.random()
        if param > 0:
            return -param*(m.log(1-rnd))
        elif param < 0:
            return (-1/param)*(m.log(1-rnd))
        else:
            raise ValueError("El parametro no puede ser cero")
    else:
        if rnd < 0 or rnd > 1:
            raise ValueError("El valor de RND debe estar entre 0 y 1")
        else: 
            if param > 1:
                return -param*(m.log(1-rnd))
            elif param < 1 and param > 0:
                return (-1/param)*(m.log(1-rnd))
            else:
                raise ValueError("El parametro no puede ser cero")
#GENERACION DE VARIABLES CON DISTRIBUCION NORMAL POR BOX-MÜLLER
def numerosNormalBoxMuller(media,des,rnd1=None,rnd2=None):
    if rnd1 is None and rnd2 is None:
        rnd1 = r.random()
        rnd2 = r.random()
        if des<=0:
            raise ValueError("La desviacion estandar no puede ser cero o negativa")
        z1 = m.sqrt(-2*m.log(rnd1))*m.cos(2*m.pi*rnd2)
        z2 = m.sqrt(-2*m.log(rnd1))*m.sin(2*m.pi*rnd2)
        n1 = z1*des+media
        n2 = z2*des+media
        return [n1,n2]
    else:
        if rnd1 < 0 or rnd1 > 1:
            raise ValueError("El valor de RND1 debe estar entre 0 y 1")
        if rnd2 < 0 or rnd2 > 1:
            raise ValueError("El valor de RND2 debe estar entre 0 y 1")
        if des<=0:
            raise ValueError("La desviacion estandar no puede ser cero o negativa")
        z1 = m.sqrt(-2*m.log(rnd1))*m.cos(2*m.pi*rnd2)
        z2 = m.sqrt(-2*m.log(rnd1))*m.sin(2*m.pi*rnd2)
        n1 = z1*des+media
        n2 = z2*des+media
        return [n1,n2]
#GENERACION DE VARIABLES CON DISTRIBUCION NORMAL POR CONVOLUCION
import random as r
def numeroNormalConvolucion(media, des, n=None, rnd=None):
    if des <= 0:
        raise ValueError("La desviación estándar no puede ser cero o negativa")
    if rnd is None:
        if n is None or n <= 0:
            raise ValueError("El valor de n debe ser un entero positivo")
        rnd = [r.random() for _ in range(n)]  
    elif isinstance(rnd, list):
        n = len(rnd) 
    else:
        raise ValueError("El valor de rnd debe ser una lista de números aleatorios")
    suma = sum(rnd) 
    z = (suma - n / 2) * des + media 
    return z
#GENERACION DE VARIABLES CON DISTRIBUCION DE POISSON
def numeroPoisson(lambd):
    if lambd <= 0:
        raise ValueError("El valor de lambda debe ser mayor que cero")
    p = 1
    x = -1
    A = m.exp(-lambd)
    while p >= A:
        rnd = r.random()
        p = p * rnd
        x += 1
    return x
        
lambd = float(Fraction(5,60))
print(m.exp(-lambd))
x = numeroPoisson(lambd)
print(x)
