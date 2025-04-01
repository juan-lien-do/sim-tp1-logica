#IMPORTACION DE LIBRERIAS
import math as m
import random as r
from fractions import Fraction
from scipy.stats import chi2,ksone
from itertools import accumulate
#GENERACION DE VARIABLES CON DISTRIBUCION UNIFORME
def numeroUniforme(a, b, rnd=None):
    if b <= a:
        raise ValueError("El valor de b debe ser mayor que a")
    
    if rnd is None:
        rnd = r.random() 
    
    if not (0 <= rnd <= 1):
        raise ValueError("El valor de RND debe estar entre 0 y 1")
    
    return round((a + (b - a) * rnd),4)
    #PREGUNTAR EL REDONDEO A 4 DIGITOS
#GENERACION DE VARIABLES CON DISTRIBUCION EXPONENCIAL NEGATIVA
def numeroExponencial(param, rnd=None):
    if param == 0:
        raise ValueError("El parametro no puede ser cero")

    if rnd is None:
        rnd = r.random()

    if not (0 <= rnd <= 1):
        raise ValueError("El valor de RND debe estar entre 0 y 1")

    if param > 1:
        return round((-param * m.log(1 - rnd)),4)
    elif param > 0 and param < 1:  
        return round((-1 / param) * m.log(1 - rnd),4)
    else:
        raise ValueError("El valor debe ser un numero positivo")
#GENERACION DE VARIABLES CON DISTRIBUCION NORMAL POR BOX-MÜLLER
def numerosNormalBoxMuller(media, des, rnd1=None, rnd2=None):

    if des <= 0:
        raise ValueError("La desviacion estandar no puede ser cero o negativa")
    

    if rnd1 is None or rnd2 is None:
        rnd1 = rnd1 or r.random()
        rnd2 = rnd2 or r.random()


    if not (0 <= rnd1 <= 1):
        raise ValueError("El valor de RND1 debe estar entre 0 y 1")
    if not (0 <= rnd2 <= 1):
        raise ValueError("El valor de RND2 debe estar entre 0 y 1")

    z1 = m.sqrt(-2 * m.log(rnd1)) * m.cos(2 * m.pi * rnd2)
    z2 = m.sqrt(-2 * m.log(rnd1)) * m.sin(2 * m.pi * rnd2)

    n1 = round((z1 * des + media),4)
    n2 = round((z2 * des + media),4)

    return [n1, n2]
#GENERACION DE VARIABLES CON DISTRIBUCION NORMAL POR CONVOLUCION
def numeroNormalConvolucion(media, des,n=None,rnd=None):
    if des <= 0:
        raise ValueError("La desviación estándar no puede ser cero o negativa")
    
    if rnd is None:
        if n is None or n <= 0:
            raise ValueError("El valor de n debe ser un entero positivo")
        suma = sum(r.random() for _ in range(n))
    elif isinstance(rnd, list):
        n = len(rnd)
        suma = sum(rnd)
    else:
        raise ValueError("El valor de rnd debe ser una lista de números aleatorios")
    
    z = (suma - n / 2) * des + media
    return round(z,4)
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
#GENERACION DE VARIABLES CON EL METODO DE CONGRUENCIA LINEAL
def numeroCongruenciaLineal(seed,k,c,g):
    if g < 0:
        raise ValueError("El valor de g debe ser positivo.")
    elif k < 0:
        raise ValueError("El valor de k debe ser positivo.")
    mod = 2**g
    if m.gcd(c,mod) != 1:
        raise ValueError("Los valores de c y m deben ser relativamente primos")
    N = mod
    a = 1+4*k
    rnd = []
    x = []
    for i in range(N):
        if i==0:
            b = a*seed + c
            x_i = round((b % mod),4)
            x.append(x_i)
        else:
            r = round((x[i-1] / (mod-1)),4)
            rnd.append(r)
            b = a*x[i-1] + c
            x_i = round((b % mod),4)
            x.append(x_i)
    v = round((x[N -1] / (mod - 1)),4)
    rnd.append(v)
    return rnd,x
#GENERACION DE VARIABLES CON EL METODO CONGRUENCIAL MULTIPLICATIVO
def numeroCongruencialMultiplicativo(seed,k,g):
    if seed % 2 == 0:
        raise ValueError("La semilla debe ser impar")
    elif k<0 and type(k) != int:
        raise ValueError("EL valor de k debe ser un entero positivo")
    elif g < 0 and type(g) != int:
        raise ValueError("El numero g debe ser un entero positivo")
    mod = 2**g
    a = 3 + 8*k
    N = 2**(g-2)
    rnd = []
    x = []
    for i in range(N):
        if i == 0:
            b = a * seed
            x_i = round((b % mod),4)
            x.append(x_i)
        else:
            y = round((x[i-1] / (mod - 1)),4)
            rnd.append(y)
            b = a * x[i-1]
            x_i = round((b % mod),4)
            x.append(x_i)
    z = round((x[N-1] / (mod - 1)),4)
    rnd.append(z)
    return rnd,x
#TEST DE PRUEBA DE CHI CUADRADO
def testPruebaChiCuadrado(rnd,a,mo=None):
    if type(rnd) != list or len(rnd) == 0:
        raise ValueError("Debe ser una lista de numeros")
    for p in rnd:
        if p >1 or p<0:
            raise ValueError("Todos los numeros deben ser de entre 0 a 1")
    n = len(rnd)
    k = m.floor(m.sqrt(n))
    if mo is None:
        v = k -1
    else:
        v = k -1 - mo
    observados = [0] * k
    esp = int(n / k)
    esperados = [esp] * k
    l_i = 0
    l_s = 1 / k
    x_2_calc = 0
    c = [0] * k
    for i in range(k):
        obs = 0
        for j in rnd:
            if l_i < j < l_s:
                obs += 1
        observados[i] += obs
        l_i = l_s
        l_s += 1 / k
        x = ((observados[i]-esperados[i])**2)/(esperados[i])
        c[i] += x
        x_2_calc += x
    alfa = 1 - a
    x_2_tabla = chi2.ppf(alfa,v)
    return observados,esperados,c,x_2_calc,x_2_tabla
#TEST DE PRUEBAS DE KOLMOGOROV SMIRNOV
def testPruebaKS(rnd,alpha):
    if type(rnd) != list or len(rnd) == 0:
        raise ValueError("Debe ser una lista de numeros")
    for p in rnd:
        if p >1 or p<0:
            raise ValueError("Todos los numeros deben ser de entre 0 a 1")
    n = len(rnd)
    k = m.floor(m.sqrt(n))
    observados = [0] * k
    esp = int(n / k)
    esperados = [esp] * k
    l_i = 0
    l_s = 1 / k
    prob_obs = [0] * k
    prob_esp = [ esp / n] * k
    
    for i in range(k):
        obs = 0
        for j in rnd:
            if l_i < j < l_s:
                obs += 1
        observados[i] += obs
        prob_obs[i] += obs / n
        l_i = l_s
        l_s += 1 / k
    apfo = list(accumulate(prob_obs))
    apfe = list(accumulate(prob_esp))
    dif = [0] * k
    for i in range(k):
        v = apfo[i] - apfe[i]
        dif[i] += v
    x=max(dif)
    k_s_tabla = ksone.ppf(1- alpha /2 ,n)
    return observados,esperados,prob_obs,prob_esp,apfo,apfe,x,k_s_tabla
    

